const CSVAnalyzer = require("./CSVAnalyzer.js");
const ContractAnalyzer = require("./ContractAnalyzer.js");
const RegistryAnalyzer = require("./UserRegistryAnalyzer.js");
const UserInputAnalyzer = require("./UserInputAnalyzer.js");

class Analyzer {

  constructor(csvPath, contractInfoPath, userRegistryPath, userInputPath) {
    this._csv_analyzer = new CSVAnalyzer(csvPath);
    this._contract_analyzer = new ContractAnalyzer(contractInfoPath);
    this._registry_analyzer = new RegistryAnalyzer(userRegistryPath);
    this._user_input_analyzer = new UserInputAnalyzer(userInputPath);
  }

  // ContractAnalyzer
  //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  get distribution_startdate() {
    return this._contract_analyzer.distribution_startdate;
  }

  get distribution_enddate() {
    return this._contract_analyzer.distribution_enddate;
  }

  get price_specification() {
    return this._contract_analyzer.price_specification;
  }

  get license() {
    return this._contract_analyzer.license;
  }

  get copyrightHolderName() {
    return this._contract_analyzer.copyrightHolderName;
  }

  get copyrightHolderMail() {
    return this._contract_analyzer.copyrightHolderMail;
  }

  get contract_startdate() {
    return this._contract_analyzer.contract_startdate;
  }

  get contract_enddate() { return this._contract_analyzer.contract_enddate; }

  get contract_description() {
    return this._contract_analyzer.contract_description;
  }
  get permissions() {
    return this._contract_analyzer.permissions;
  }
  get sanctions() {
    return this._contract_analyzer.sanctions;
  }

  get negotiation_protocol() {
    return this._contract_analyzer.negotiation_protocol;
  }


  get access_rights() { return this._contract_analyzer.access_rights; }

  // CSVAnalyzer
  //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  get metadata_name() { return this._csv_analyzer.metadata_name; }

  get metadata_type() { return this._csv_analyzer.metadata_type; }

  get metadata_size() { return this._csv_analyzer.metadata_size; }

  get metadata_date() { return this._csv_analyzer.metadata_date; }

  get csv_data() { return this._csv_analyzer.csv_data; }

  get properties() { return this._csv_analyzer.properties; }

  get datatypes() { return this._csv_analyzer.datatypes; }

  // UserInputAnalyzer
  //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  get accrual_periodicity() {
    return this._user_input_analyzer.accrual_periodicity;
  }

 // get contributor_name() { return this._user_input_analyzer.contributor_name; }

 // get contributor_url() { return this._user_input_analyzer.contributor_url; }

  get file_description() { return this._user_input_analyzer.description; }

  get conformsToStandard() { return this._user_input_analyzer.conformsToStandard; }

  get standardReference() { return this._user_input_analyzer.standardReference; }

  get localURL() { return this._user_input_analyzer.localURL; }

 // get temporal_startdate() {
 //   return this._user_input_analyzer.temporal_startdate;
 // }

 //  get temporal_enddate() { return this._user_input_analyzer.temporal_enddate; }

  get version_description() { return this._user_input_analyzer.version_description; }

  get qualityScore() {
    return this._user_input_analyzer.qualityScore;
  }
  get accuracy() {
    return this._user_input_analyzer.accuracy;
  }
  get unit() {
    return this._user_input_analyzer.unit;
  }

  // UserRegistryAnalyzer
  //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  get provenance_name() { return this._registry_analyzer.provenance_name; }

  get provenance_url() { return this._registry_analyzer.provenance_url; }

  get gaxAcronym() { return this._registry_analyzer.gaxAcronym; }

  get certificates() { return this._registry_analyzer.certificates; }

 // get reputation() { return this._registry_analyzer.reputation; }

  get provenance_street() {
    return this._registry_analyzer.provenance_street;
}

get provenance_locality() {
    return this._registry_analyzer.provenance_locality;
}

get provenance_country() {
    return this._registry_analyzer.provenance_country;
}

get provenance_jurisdiction() {
    return this._registry_analyzer.provenance_jurisdiction;
}

get provenance_SalesTaXID() {
    return this._registry_analyzer.provenance_SalesTaXID;
}

get provenance_legalRegistrationNumber() {
    return this._registry_analyzer.provenance_legalRegistrationNumber;
}

get provenance_legalContactName() {
    return this._registry_analyzer.provenance_legalContactName;
}

get provenance_legalContactEmail() {
    return this._registry_analyzer.provenance_legalContactEmail;
}

get provenance_technicalContactName() {
    return this._registry_analyzer.provenance_technicalContactName;
}

get provenance_technicalContactEmail() {
    return this._registry_analyzer.provenance_technicalContactEmail;
}
}

module.exports = Analyzer;
