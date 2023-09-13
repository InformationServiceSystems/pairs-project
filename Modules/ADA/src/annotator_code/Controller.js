const Analyzer = require('./DataReaderAndAnalyzer/Analyzer.js');
const BabelnetAdapter = require('./BabelnetAdapter.js');

class Controller {

  constructor(csvPath, contractInfoPath, userRegistryPath, userInputPath) {
    this._analyzer = new Analyzer(csvPath, contractInfoPath, userRegistryPath,
                                 userInputPath);
    this._babelnetAdapter = new BabelnetAdapter(this._analyzer.metadata_name, this._analyzer.properties);
    this._dpdo_class = "Datafile";
  }

  // creates date for modified
  createmodified() {
    // const now = new Date();
    // const result = now.getDate() + "-" + (now.getMonth() + 1) + "-" +
    //                now.getFullYear() + "   " + now.getHours() + ":" +
    //                now.getMinutes() + ":" + now.getSeconds() + "." +
    //                now.getMilliseconds();
    const result = new Date();
    return result;
  }

  get timeStamp() {
    const stamp = Date.now();
    return stamp;
  }

  // create a new version using situations
  createVersion() {

    const version =
        "           \"dct:isVersionOf\": {\r\n" +
        "				\"schema:description\": \"" +
        this._analyzer.version_description + "\",\r\n" +
        "				\"dpdo:type\": \"" +
        "UpdateOf" +
        "\",\r\n" +
        "				\"gax-DataServiceOffering:wasCreatedOn\": \"" + this.createmodified() + "\"\r\n" +
        "	}\r\n"

    return version;
  }

  get identifier() {
    const identifier = "https://spaicer.de/dpdo/" + Math.floor(Math.random() * 1000000);
    return identifier
  }

  get context() {
    const context =
        "{\r\n" +
        "	\"@context\": [{\r\n" +
        "		\"schema\": \"http://schema.org\",\r\n" +
        "		\"dcat\": \"http://www.w3.org/ns/dcat#\", \r\n" +
        "		\"dct\": \"http://purl.org/dc/terms/\", \r\n" +
        "		\"dqm\": \"http://semwebquality.org/dqm-vocabulary/v1/dqm#\",\r\n" +
        "		\"ov\": \"http://open.vocab.org/terms/#\", \r\n" +
        "		\"dpdo\": \"http://dpdo.org/dpdo#\",\r\n" +
        "		\"gax-participant\": \"http://w3id.org/gaia-x/participant#/\", \r\n" +
        "		\"gax-DataServiceOffering\": \"http://w3id.org/gaia-x/core#DataServiceOffering\", \r\n" +
        "		\"gax-provider\": \"http://w3id.org/gaia-x/participant#Provider\", \r\n" +
        "		\"gax-asset\": \"http://w3id.org/gaia-x/asset#/\", \r\n" +
        "		\"vcard\": \"http://www.w3.org/2006/vcard/ns\" \r\n" +
        "	}],\r\n";
    return context;
  }

  get product_description() {
    const product_description =
        "	\"dpdo:ProductDescriptionFacet\": {\r\n" +
        "    	\"@id\": \"" + this.identifier + "\",\r\n" +
        "    	\"gax-DataServiceOffering:hasServiceTitle\": \"" + this._analyzer.metadata_name + "\",\r\n" +
        "    	\"dcat:theme\": \"" + this._babelnetAdapter.getTheme() + "\",\r\n" +
        "    	\"dpdo:subcategory\": \"" + this._babelnetAdapter.getSubcategory() + "\",\r\n" +
        "		  \"gax-DataServiceOffering:hasType\": \"" + this._dpdo_class + "\",\r\n" +
        "		  \"gax-DataServiceOffering:hasServiceDescription\": \"" + this._analyzer.file_description + "\",\r\n" +
        "    	\"dct:accrualPeriodicity\": \"" + this._analyzer.accrual_periodicity + "\",\r\n" +
        "     \"gax-DataServiceOffering:hasContentType\": \"" + this._analyzer.metadata_type + "\",\r\n" +
        "    	\"gax-DataServiceOffering:hasContentLength\": \"" + this._analyzer.metadata_size + "Bytes\",\r\n" +
        "    	\"ov:csvcol\": \"" + this._analyzer.properties + "\",\r\n" +
        "    	\"schema:DataType\": \"" + this._analyzer.datatypes + "\"\r\n" +
        " },\r\n";
    return product_description;
  }

  get quality_description() {
    const quality_description =
        "	\"dpdo:QualityDescriptionFacet\": {\r\n" +
        "    	\"@id\": \"" + this.identifier + "\",\r\n" +
        "     \"gax-DataServiceOffering:conformsToStandard\": \"" + this._analyzer.conformsToStandard + "\",\r\n" +
        "     \"gax-DataServiceOffering:StandardReference\": \"" + this._analyzer.standardReference + "\",\r\n" +
        "		  \"dqm:DataQualityScore\": {\r\n" +
        "         	\"@id\": \"" + this.identifier + "\",\r\n" +
        "		        \"dqm:plainScore\": \"" + this._analyzer.qualityScore + "\",\r\n" +
        "		        \"dqm:unitOfMeasurement\": \"" + this._analyzer.unit + "\"\r\n" +
        "    	       },\r\n" +
        "		  \"dqm:Accuracy\": {\r\n" +
        "         	\"@id\": \"" + this.identifier + "\",\r\n" +
        "		        \"dqm:plainScore\": \"" + this._analyzer.accuracy + "\",\r\n" +
        "		        \"dqm:unitOfMeasurement\": \"" + this._analyzer.unit + "\"\r\n" +
        "    	       }\r\n" +
        " },\r\n";
    return quality_description;
  }

  get usage_description() {
    const usage_description = "\"dpdo:UsageDescriptionFacet\": {\r\n" +
                              "    	\"@id\": \"" + this.identifier + "\",\r\n" +
                              "     \"gax-DataServiceOffering:hasLocalURL\": \"" + this._analyzer.localURL + "\",\r\n" +
                              "    	\"dct:modified\": \"" + this._analyzer.metadata_date + "\",\r\n" +
                              "    	\"dct:hasVersion\": {\r\n" +
                              "       	\"@id\": \"" + this.identifier + "\",\r\n" + this.createVersion()  +   
                              "	},\r\n" +
                              "    	\"dcat:Distribution\": {\r\n" +
                              "    	  \"@id\": \"" + this.identifier + "\",\r\n" +
                              "    		\"dct:PeriodOfTime\": {\r\n" +
                              "    	    \"@id\": \"" + this.identifier + "\",\r\n" +
                              "    		   \"dcat:startDate\": \"" + this._analyzer.distribution_startdate + "\",\r\n" +
                              "    	    	\"dcat:endDate\": \"" + this._analyzer.distribution_enddate + "\"\r\n" +
                              "		}\r\n" +
                              "    	},\r\n" +
                              "           \"gax-participant:IndividualContactTechnical\": {\r\n" +
                              "    	            \"vcard:givenName\": \"" + this._analyzer.provenance_technicalContactName + "\",\r\n" +
                              "    	            \"vcard:hasEmail\": \"" + this._analyzer.provenance_technicalContactEmail + "\"\r\n" +
                              "    	       }\r\n" +
                              "  	},\r\n	";
    return usage_description;
  }

  get business_description() {
    const business_description =
        "\"dpdo:BusinessDescriptionFacet\": {\r\n" +
        "    	\"@id\": \"" + this.identifier + "\",\r\n" +
        "     \"gax-DataServiceOffering:hasLicense\": \"" + this._analyzer.license + "\",\r\n" +
        "           \"gax-DataServiceOffering:hasCopyrightHolder\": {\r\n" +
        "    	            \"vcard:givenName\": \"" + this._analyzer.copyrightHolderName + "\",\r\n" +
        "    	            \"vcard:hasEmail\": \"" + this._analyzer.copyrightHolderMail + "\"\r\n" +
        "    	       },\r\n" +
        "    	\"schema:PriceSpecification\": \"" +
        this._analyzer.price_specification + "\",\r\n" +
        "    	\"proton:Contract\": " +
        "{\r\n" +
        "    	  \"@id\": \"" + this.identifier + "\",\r\n" +
        "			\"dcat:startDate\": \"" +
        this._analyzer.contract_startdate + "\",\r\n" +
        "    		\"dcat:endDate\": \"" + this._analyzer.contract_enddate +
        "\",\r\n" +
        "    		\"schema:description\": \"" +
        this._analyzer.contract_description + "\",\r\n" +
        "    		\"dpdo:Permissions\": \"" +
        this._analyzer.permissions + "\",\r\n" +
        "    		\"dpdo:Sanctions\": \"" +
        this._analyzer.sanctions + "\"\r\n" +
        "		},\r\n" +
        "    	\"dpdo:NegotiationProtocol\": {\r\n" +
        "    		\"schema:description\": \"" + this._analyzer.negotiation_protocol + "\"\r\n" +
        "		}\r\n" +
        "  	},\r\n	";
    return business_description;
  }

  get trustandsecurity_description() {
    const trustandsecurity_description =
        "\"dpdo:TrustDescriptionFacet\": {\r\n" +
        "    	\"@id\": \"" + this.identifier + "\",\r\n" +
        "     \"gax-asset:owned_by\": \"" + this._analyzer.gaxAcronym + "\",\r\n" +
        "		  \"dct:Provenance\": {\r\n" +
        "		        \"gax-participant:Provider\": {\r\n" +
        "     	   	\"gax-participant:hasLegallyBindingName\": \"" + this._analyzer.provenance_name + "\",\r\n" +
        "      	   	\"gax-participant:hasLegallyBindingAddress\": {\r\n" +
        "                	\"@id\": \"" + this.identifier + "\",\r\n" +
        "    	            \"vcard:street-address\": \"" + this._analyzer.provenance_street + "\",\r\n" +
        "    	            \"vcard:locality\": \"" + this._analyzer.provenance_locality + "\",\r\n" +
        "    	            \"vcard:country-name\": \"" + this._analyzer.provenance_country + "\"\r\n" +
        "    	       },\r\n" +
        "     	   	\"gax-provider:hasWebAddress\": \"" + this._analyzer.provenance_url + "\",\r\n" +
        "     	   	\"gax-provider:hasJurisdiction\": \"" + this._analyzer.provenance_jurisdiction + "\",\r\n" +
        "     	   	\"gax-provider:hasSalesTaxID\": \"" + this._analyzer.provenance_SalesTaXID + "\",\r\n" +
        "     	   	\"gax-provider:hasLegalRegistrationNumber\": \"" + this._analyzer.provenance_legalRegistrationNumber + "\",\r\n" +
        "     	   	\"gax-participant:hasIndividualContactLegal\": {\r\n" +
        "    	            \"vcard:givenName\": \"" + this._analyzer.provenance_legalContactName + "\",\r\n" +
        "    	            \"vcard:hasEmail\": \"" + this._analyzer.provenance_legalContactEmail + "\"\r\n" +
        "    	       }\r\n" +
        "    	  }\r\n" +
        "   }\r\n	" +
        "	}\r\n\n\r}";
    return trustandsecurity_description;
  }

  get dpdo() {

    return this.context + this.product_description + this.quality_description + this.usage_description +
           this.business_description + this.trustandsecurity_description;
  }
}

module.exports = Controller;