const fs = require('fs');

class ContractAnalyzer {
    constructor(contractInfoPath) {
        const data = fs.readFileSync(contractInfoPath, 'utf8');
        console.log(contractInfoPath);
        console.log(data);
        this._data = JSON.parse(data);
    }

    get distribution_startdate() {
        return new Date(this._data["distribution_startdate"]);
    }

    get distribution_enddate() {
        return new Date(this._data["distribution_enddate"]);
    }

    get price_specification() {
        return this._data["price_specification"];
    }

    get license() {
        return this._data["license"];
    }

    get copyrightHolderName() {
        return this._data["copyrightHolder_name"];
    }
    get copyrightHolderMail() {
        return this._data["copyrightHolder_mail"];
    }

    get contract_startdate() {
        return new Date(this._data["contract_startdate"]);
    }

    get contract_enddate() {
        return new Date(this._data["contract_enddate"]);
    }

    get contract_description(){
        return this._data["contract_description"];
    }

    get permissions(){
        return this._data["permissions"];
    }

    get sanctions(){
        return this._data["sanctions"];
    }
    
    get negotiation_protocol() {
        return this._data["negotiation_protocol"];
    }

    get access_rights() {
        return this._data["rights"];
    }
}

module.exports = ContractAnalyzer;
