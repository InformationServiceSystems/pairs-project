const path = require('path');
const fs = require('fs');
const neo4j = require('neo4j-driver');


class Neo4jEngine {
  constructor(scriptPath, dpdoPath) {
    this._scriptPath = scriptPath;
    this._dpdoPath = dpdoPath;
  }

  async  neo4jTest() {
    const db = neo4j.driver("bolt://localhost:7687");
    const result = await db
    .session({
      database: "neo4j",
      defaultAccessMode: neo4j.session.WRITE,
    })
    // .run("CREATE (n:Testnode {label3: 'test3', label4: 'tets4'}) CREATE (n)-[r:RELTYPE]->(m)");
    .run(this.getScript());
    console.log(this.getScript());
    //.run(this._scriptPath);
    await result;
     return this.getScript();
  }

  getScript() {
    var script = fs.readFileSync(this._scriptPath, 'utf-8');
    var result = script.replace(/XXXXX/g, this._dpdoPath);
    return result;
  }

}

module.exports = Neo4jEngine;
