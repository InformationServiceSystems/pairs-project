const http = require('express').Router()
const path = require('path')
const fs = require('fs')
const fsExtra = require('fs-extra')

const ProvisionEngine = require('../annotator_code/ProvisionEngine');
const Neo4jEngine = require('../annotator_code/Neo4jEngine');

http.get('/', async (req, res) => {
  res.sendFile(path.join(__dirname, '/html/annotate.html'));
});

http.get('/annotate', async (req, res) => {
  res.sendFile(path.join(__dirname, '/html/annotate.html'));
});

//http.post('/annotate', async (req, res) => {
//  //try {
//  const anbieter_vorname = req.body.anbieter_vorname;
//  const anbieter_nachname = req.body.anbieter_nachname;
//  const anbieter_firma = req.body.anbieter_firma;
//  const anbieter_url = req.body.anbieter_url;
//  const anbieter_strasse = req.body.anbieter_strasse;
//  const vertrag_preis = req.body.vertrag_preis;
//  const vertrag_start = req.body.vertrag_start;
//  const vertrag_ende = req.body.vertrag_ende;
//  const vertrag_beschreibung = req.body.vertrag_beschreibung;
//  const vertrag_verhandlung = req.body.vertrag_verhandlung;
//  const anbieter_stadt = req.body.anbieter_stadt;
//  const anbieter_land = req.body.anbieter_land;
//  const anbieter_plz = req.body.anbieter_plz;
//  const mitwirkende_vorname = req.body.mitwirkende_vorname;
//  const mitwirkende_nachname = req.body.mitwirkende_nachname;
//  const mitwirkende_firma = req.body.mitwirkende_firma;
//  const mitwirkende_url = req.body.mitwirkende_url;
//  const beschreibung_inhalt = req.body.beschreibung_inhalt;
//  const beschreibung_start = req.body.beschreibung_start;
//  const beschreibung_ende = req.body.beschreibung_ende;
//  const beschreibung_bereitstellung = req.body.beschreibung_bereitstellung;
//  const nutzung_version = req.body.nutzung_version;
//  const nutzung_referenz = req.body.nutzung_referenz;
//  const nutzung_start = req.body.nutzung_start;
//  const nutzung_ende = req.body.nutzung_ende;
//  const sicherheit_rechte = req.body.sicherheit_rechte;
//  const sicherheit_zertifikate = req.body.sicherheit_zertifikate;

//  const sampleFile = req.files.csv;
//  console.log("SampleFile: " + sampleFile.name);
//  let uploadPath= path.join(__dirname, 'createdSamples/Messdaten_Anlage_Drucklufterzeugung.csv');
//  console.log("Upload Path: " + uploadPath);
//  //sampleFile.mv(uploadPath, function(err) {console.log("Fehler: " + err)});
//  fs.writeFileSync(uploadPath, sampleFile.data);


//  let userInput = 
//  {
//      "accrual_periodicity": beschreibung_bereitstellung,
//      "contributor_name":  mitwirkende_vorname + " " + mitwirkende_nachname,
//      "contributor_url": mitwirkende_url,
//      "description": beschreibung_inhalt,
//      "temporal_startdate": beschreibung_start,
//      "temporal_enddate": beschreibung_ende,
//      "version_description": nutzung_version,
//  }
//  let userRegistry = 
//  {
//    "provenance_name": anbieter_vorname + " " + anbieter_nachname,
//    "provenance_url": anbieter_url,
//    "certificates": sicherheit_zertifikate
//}
//let contract = 
//  {
//    "distribution_startdate": nutzung_start,
//    "distribution_enddate": nutzung_ende,
//    "price_specification": vertrag_preis,
//    "contract_startdate": vertrag_start,
//    "contract_enddate": vertrag_ende,
//    "contract_description": vertrag_beschreibung,
//    "negotiation_protocol": vertrag_verhandlung,
//    "access_rights": sicherheit_rechte }


//  let userInput_data = JSON.stringify(userInput);
//  fs.writeFileSync(path.join(__dirname, 'createdSamples/userInput.json'), userInput_data);
//  let userRegistry_data = JSON.stringify(userRegistry);
//  fs.writeFileSync(path.join(__dirname, 'createdSamples/userRegistry.json'), userRegistry_data);
//  let contract_data = JSON.stringify(contract);
//  fs.writeFileSync(path.join(__dirname, 'createdSamples/contract.json'), contract_data);

//  // TODO: Pfad anpassen nachdem inputs gemapt wurden
//  const provisionEngine = new ProvisionEngine(
//   path.join(__dirname, 'createdSamples/Messdaten_Anlage_Drucklufterzeugung.csv'),path.join(__dirname, 'createdSamples/contract.json'),
//    path.join(__dirname, 'createdSamples/userRegistry.json'), path.join(__dirname, 'createdSamples/userInput.json'));
//  const dpdo = provisionEngine.getDPDO();
//  fs.writeFileSync(path.join(__dirname, 'createdSamples/dpdo.json'), dpdo);

//  res.download(path.join(__dirname, 'createdSamples/dpdo.json'));
//  //} catch(err) {
//  //  res.status(400).send(err)
//  //}
//});

http.get('/dpdo', async (req, res) => {
  let rawdata = fs.readFileSync(path.join(__dirname, 'uploads', 'dpdo.json'));
  let data = JSON.parse(rawdata);
  res.json(data);
})

http.get('/knowledge', async (req, res) => {
  res.sendFile(path.join(__dirname, '/html/knowledge.html'));
});

http.post('/knowledge', async (req, res) => {
  const revisedDPDO = req.files.dpdo;
  console.log("RevisedDPDO: " + revisedDPDO.name);
  let uploadPath= path.join(__dirname, 'uploads', 'dpdo.json');
  revisedDPDO.mv(uploadPath, function(err) {});
  try {
    const neo4jEngine = new Neo4jEngine(path.join(__dirname, 'createdSamples/JsonToCypherScript.cyp'), 'http://localhost:8080/interface/dpdo');
    const dpdo = neo4jEngine.neo4jTest();
    res.redirect("http://localhost:7474");
  } catch (err) {
    res.status(500).send("error occured: " + err);
  }
});

http.post('/annotate', async (req, res) => {
  const uploads = req.files.uploads;
  fsExtra.emptyDirSync(path.join(__dirname, 'uploads'));
  let contract = null;
  let registry = null;
  let userInput = null;
  let csv = null;
  if (uploads.length != 4) {
    res.status(500).send("Please submit the correct files");
 }
  for (let i = 0; i < uploads.length; i++) {
    let uploadPath= path.join(__dirname, 'uploads', uploads[i].name);
    console.log("Uploaded: " + uploads[i].name);
    uploads[i].mv(uploadPath, function(err) {
      // console.log("Failed to upload to: " + uploadPath)
    });
    if (uploads[i].name == "contract.json") {
      contract = uploadPath;  
    }
    else if (uploads[i].name == "userRegistry.json") {
      registry = uploadPath;
    }
    else if (uploads[i].name == "userInput.json") {
      userInput = uploadPath;
    }
    else {
      csv = uploadPath;
    }
  }
  console.log(contract);
  console.log(registry);
  console.log(userInput);
  console.log(csv);
  await new Promise(resolve => setTimeout(resolve, 5000));
  const provisionEngine = new ProvisionEngine(csv , contract, registry, userInput)
  const dpdo = provisionEngine.getDPDO();
  fs.writeFileSync(path.join(__dirname, 'uploads', 'dpdo.json'), dpdo);
  try {
    
    //const neo4jEngine = new Neo4jEngine(path.join(__dirname, 'createdSamples/JsonToCypherScript.cyp'), 'http://spaicer:8080/interface/dpdo');
    //const dpdo = neo4jEngine.neo4jTest();
    res.download(path.join(__dirname, 'uploads', 'dpdo.json'));
    //res.redirect("http://localhost:7474");
  } catch (err) {
    res.status(500).send("error occured: " + err);
  }
});

http.get('/dpdoDownload', async (req, res) => {
  res.download(path.join(__dirname, 'uploads/dpdo.json'));
});

http.get('/sampleContract', async (req, res) => {
  res.download(path.join(__dirname, 'createdSamples/contract.json'));
});

http.get('/sampleRegistry', async (req, res) => {
  res.download(path.join(__dirname, 'createdSamples/userRegistry.json'));
});

http.get('/sampleUserInput', async (req, res) => {
  res.download(path.join(__dirname, 'createdSamples/userInput.json'));
});

module.exports = http
