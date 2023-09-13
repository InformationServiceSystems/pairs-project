const fs = require('fs');

class UserInputAnalyzer {
    constructor(userInputPath) {
        this._data = JSON.parse(fs.readFileSync(userInputPath));
    }

    get accrual_periodicity() {
        return this._data["accrual_periodicity"];
    }

    get contributor_name() {
        return this._data["contributor_name"];
    }

    get contributor_url() {
        return this._data["contributor_url"];
    }

    get description() {
        return this._data["description"];
    }

    get conformsToStandard() {
        return this._data["conformsToStandard"];
    }
    get standardReference() {
        return this._data["StandardReference"];
    }

    get localURL() {
        return this._data["localURL"];
    }
    
 //   get temporal_startdate() {
  //      return new Date(this._data["temporal_startdate"]);
  //  }

  //  get temporal_enddate() {
  //      return new Date(this._data["temporal_enddate"]);
   // }
    get version_description() {
        return this._data["version_description"];
    }
    get qualityScore() {
        return this._data["dataQualityScore"];
    }

    get accuracy() {
        return this._data["dataAccuracy"];
    }
    get unit() {
        return this._data["scoreUnit"];
    }

}    

module.exports = UserInputAnalyzer;