const path = require('path');
const fs = require('fs');
const Controller = require('./Controller.js');
const neo4j = require('neo4j-driver');


class ProvisionEngine {
  constructor(csvPath, contractInfoPath, userRegistryPath, userInputPath) {
    this._controller = new Controller(csvPath, contractInfoPath,
                                      userRegistryPath, userInputPath);
  }

  getDPDO() {
    console.log('test');
    console.log(this._dpdo);
     return this._controller.dpdo;
  }

  writeDPDO(outPath) {
    const outFile = path.join(outPath, 'dpdo.json');
    fs.writeFileSync(outFile, this._controller.dpdo);
  }
}

module.exports = ProvisionEngine;
