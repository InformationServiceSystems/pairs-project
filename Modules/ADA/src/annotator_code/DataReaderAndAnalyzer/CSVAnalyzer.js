const fs = require('fs')
const path = require('path')

class CSVAnalyzer {

  constructor(csvPath) {
    // this can read contents of the csv file metadata
    this._stats = fs.statSync(csvPath);
    this._csvPath = csvPath;

    const delimiter = ',';  // SET CSV DELIMITER HERE (e.g., comma or semicolon)

    const data = fs.readFileSync(csvPath, 'utf-8');
    const rows = data.split(/[\r\n]+/);

    this._properties = rows[0].split(delimiter); // delete possible occurrences of the " character
    this._csv_data = [];

    rows.slice(1).forEach((row) => {
      let row_data = {};
      const values = row.split(delimiter);
      values.forEach((value, i) => {
        const key = this._properties[i];
        row_data[key] = value.replace(/"/g, '');
      });
      this._csv_data.push(row_data);
    });

  }

//get datatypes in csv file
  get datatypes() {
    var csv_matrix = this._csv_data;
    var datatypes_list = [];

    // get Datatypes
    for (var j = 0; j < this.properties.length; j++) {
      var set = new Set();

      for (const [key, value] of Object.entries(csv_matrix[0])) {
        var datatype;
        if (this.properties[j] == key) {
          if (+value === parseInt(value)) {
            datatype = "Integer";
          } else if (+value === parseFloat(value)) {
            datatype = "Float";
          } else if (!Number.isNaN(Date.parse(value))) {
            datatype = "Date";
          } else if (value == 'true' || value == 'false') {
            datatype = "Boolean";
          } else {
            datatype = "String";
          }
          set.add(datatype);
        }
      }

      datatypes_list.push(set);
    }

    // create string of DataTypes
    var result = String();
    for (var j = 0; j < datatypes_list.length; j++) {
      if (j == 0) {
        result = Array.from(datatypes_list[j]).join("/");
      } else {
        result = result + ", " + Array.from(datatypes_list[j]).join("/");
      }
    }
    return result;
  }

  // Name of csv file (bsp: oranges.csv)
  get metadata_name() { return path.basename(this._csvPath); }

  // Content type / file type
  get metadata_type() { return 'csv'; }

  // Size in kb
  get metadata_size() { return this._stats.size; }

  // Creation time for csv file
  get metadata_date() { return this._stats.birthtime; }

  // Array of lines containing dict with key:values
  get csv_data() { return this._csv_data; }

  // Column names of csv file
  get properties() { return this._properties; }
}

module.exports = CSVAnalyzer;