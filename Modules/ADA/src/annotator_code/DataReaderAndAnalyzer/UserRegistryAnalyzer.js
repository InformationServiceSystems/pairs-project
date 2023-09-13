const fs = require('fs');

class UserRegistryAnalyzer {
    constructor(userRegistryPath) {
        this._data = JSON.parse(fs.readFileSync(userRegistryPath));
    }

    get provenance_name() {
        return this._data["provider_name"];
    }

    get provenance_url() {
        return this._data["provider_url"];
    }

    get provenance_street() {
        return this._data["provider_street"];
    }

    get provenance_locality() {
        return this._data["provider_locality"];
    }

    get provenance_country() {
        return this._data["provider_country"];
    }

    get provenance_jurisdiction() {
        return this._data["provider_jurisdiction"];
    }

    get provenance_SalesTaXID() {
        return this._data["provider_SalesTaxID"];
    }

    get provenance_legalRegistrationNumber() {
        return this._data["provider_legalRegistrationNumber"];
    }

    get provenance_legalContactName() {
        return this._data["legalContactName"];
    }

    get provenance_legalContactEmail() {
        return this._data["legalContactMail"];
    }

    get provenance_technicalContactName() {
        return this._data["technicalContactName"];
    }

    get provenance_technicalContactEmail() {
        return this._data["technicalContactMail"];
    }

    get gaxAcronym() {
        return this._data["gaxAcronym"];
    }

    get certificates() {
        return this._data["certificates"];
    }

 //   get reputation() {
  //      return this._data["reputation"];
  //  }
}

module.exports = UserRegistryAnalyzer;
