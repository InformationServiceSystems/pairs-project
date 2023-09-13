const http = require('express').Router()
const ProvisionEngine = require('../annotator_code/ProvisionEngine');
const Neo4jEngine = require('../annotator_code/Neo4jEngine');

http.get('/neo4j', async (req, res) => {
  try {
    const neo4jEngine = new Neo4jEngine('samples/JsonToCypherScript.cyp', 'http://spaicer:8080/example/cyp');
    const dpdo = neo4jEngine.neo4jTest();
    res.status(200).send('Data added to Neo4j successfully.');
  } catch (err) {
    res.status(500).send("error occured: " + err);
  }
});

http.get('/cyp', async (req, res) => {
  let rawdata = fs.readFileSync("/testdpdo.json");
  let data = JSON.parse(rawdata);
  res.json(data);

});

http.get('/', async (req, res) => {
  try {
    const provisionEngine = new ProvisionEngine(
      'samples/Messdaten Anlage Drucklufterzeugung.csv', 'samples/contract.json',
      'samples/userRegistry.json', 'samples/userInput.json');
    const dpdo = provisionEngine.getDPDO();
    console.log(dpdo);
    res.status(200).send(dpdo);
  } catch (err) {
    res.status(500).send("error occured: " + err);
  }
});


module.exports = http

