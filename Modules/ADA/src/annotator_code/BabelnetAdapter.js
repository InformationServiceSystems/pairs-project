var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var lemmaExtraction = require("./lemmaExtraction");

class BabelNetAdapter {

    constructor(metadataName, props) {

        this.maxNumberSyns = 5;    // limit the number of synset items (synonyms) to be checked, in order to not produce too many BN queries

        this.dataNames = lemmaExtraction.getTargetLemmas(metadataName);
        console.log("Lemma(ta): " + lemmaExtraction.cleanUpArray(this.dataNames));

        this.dataProps = props;                                 // CSV column names

        this.babelnetRequestType = {
            'getSynsetIDs': 'https://babelnet.io/v6/getSynsetIds',
            'getSynset': 'https://babelnet.io/v6/getSynset',
            'getHypernymIDs': 'https://babelnet.io/v6/getOutgoingEdges'
        };

        this.key = 'bc88251c-0637-4600-b4ed-d0a5ead92c59';      // Key Amin
        //this.key = 'b2ae88b6-0dc1-49a9-873d-59fecc8cdf1c';    // Key Natalie

        // Target output
        this.theme = '';
        this.subcategory = '';

        this.themeHasBeenSet = false;
        this.subcategoryHasBeenSet = false;

        console.log("BabelNetAdapter available.");

        // Identify theme and subcategory on creation
        this.runFullJob();
    }

    removeFileExtension(fileName) {
        // Checks if transmitted input filename has extension in it or not and if yes, remove it
        // The file name is split after the _first_ dot.
        // Example: "orange.csv.pdf" -> "orange"

        var fileNoExtension = fileName.split('.')[0];   // get everything without extension

        return fileNoExtension;
    }

    removeDuplicates(array_) {
        var ret_array = [];
        for (var a = 0; a < array_.length; a++) {
            for (var b = 0; b < array_.length; b++) {
                if(array_[a] == array_[b] && a != b){
                    delete array_[b];
                }
            }
            if(array_[a] != undefined)
                ret_array.push(array_[a]);
        }
        return ret_array;
    }

    getLemmas(fileName) {
        // TODO remove numbers
        // e.g., for input 'Measured data_plant_compressed_air_generation'
        // the output should be: ['Measured', 'data', 'plant', 'compressed', 'air', 'generation']

        // Remove spaces ' '
        var noSpaces = fileName.split(' ');

        // Remove subs '_'
        var noSubs = [];
        for (var i=0; i < noSpaces.length; i++) {
            var temp = noSpaces[i].split('_');
            for (var j=0; j < temp.length; j++) {
                noSubs.push(temp[j]);
            }
        }

        // Remove dashes '-'
        var noDashes = [];
        for (var i=0; i < noSubs.length; i++) {
            var temp = noSubs[i].split('-');
            for (var j=0; j < temp.length; j++) {
                noDashes.push(temp[j]);
            }
        } 

        // Remove duplicates
        var noDuplicates = this.removeDuplicates(noDashes);

        return noDuplicates;
    }

    formExpression(lemmas) {
        // input is an array of strings that is then composed into one string (including spaces between the strings)
        // Example: ["condition", "monitoring"] -> "condition monitoring"
        var expr = '';
        for (var i=0; i < lemmas.length; i++) {
            expr += lemmas[i];
            if (i < lemmas.length - 1) {
                expr += ' ';
            } 
        }
        return expr;
    }

    splitSpecialWords(fileName) {
        var specialWordsEN = ['of', 'for'];
        var specialWordsDE = ['von', 'für', 'zur'];
        var specialWords = specialWordsEN.concat(specialWordsDE);

        var newSplitList = fileName;

        for (var i=0; i < specialWords.length; i++) {
            if (fileName.includes(specialWords[i])) {
                newSplitList = newSplitList.split(specialWords[i]).pop();   // newSplitList contains the part of the file name following a special word
            }
        }

        return newSplitList;
    }


    runHttpRequest(queryURL) {
        var client = new XMLHttpRequest();
        client.open("GET", queryURL, false);    // false = synchronous request = stop execution until response is received
        client.send(null);
        return client.responseText;             // returns the HTTP response
    }

    getInitialBabelnetParams(lemmaIndex) {

        // Returns parameters for Babelnet request
        // input: TODO
        // output: babelnetParams (dict)

        // Default values
        //var lemma = "blanking";
        var lang1 = 'en';
        var lang2 = 'de';
        var source = '';

        var lemma = this.dataName;
        var lemmas = this.dataNames;
        var key = this.key;

        if (this.dataNames.length != 1) {
            var params = {
                //'lemma': lemma,
                'lemma': lemmas[lemmaIndex],
                'lang1': lang1,
                'lang2': lang2,
                'source': source,
                'key': key
            };
        }
        else {
            var params = {
                'lemma': lemmas,
                'lang1': lang1,
                'lang2': lang2,
                'source': source,
                'key': key
            };
        }

        return params;
    }

    runBabelnetQuery(requestType, params) {

        // returns the parsed JSON Object with the result from the Babelnet Request

        // 1. Create the URL
        var queryURL = requestType;

        if (params.lemma != '') {
            queryURL += ('?lemma=' + params.lemma);
        }

        if (params.source != '') {
            queryURL += ('&source=' + params.source);
        }

        if (params.lang1 != '') {
            queryURL += ('&searchLang=' + params.lang1);
        }

        if (params.lang2 != '') {
            queryURL += ('&searchLang=' + params.lang2);
        }

        if (params.key != '') {
            queryURL += ('&key=' + params.key);
        } else {
            console.log("Error: No valid Babelnet key.");
            return null;
        }

        // 2. Create and run HttpRequest
        var httpRes = this.runHttpRequest(queryURL);

        // 3. Convert Http response to JSON object
        var jsonRes = JSON.parse(httpRes);

        return jsonRes;
    }

    getSynset(params) {
        return this.runBabelnetQuery(this.babelnetRequestType.getSynsetIDs, params);
    }

    getHypernyms(IDs) {
        var potentialHypernymsJSON = [];
        for (var i=0; i < IDs.length; i++) {
            // construct URL
            var queryURL = 'https://babelnet.io/v6/getOutgoingEdges?id=' + IDs[i] + '&key=' + this.key;
            // request hypernyms JSON object for this synset ID
            var httpRes = this.runHttpRequest(queryURL);
            potentialHypernymsJSON.push(JSON.parse(httpRes));
        }
        
        return potentialHypernymsJSON;
    }

    extractIDsFromHypernyms(potentialHypernymsJSON) {
        var IDs = [];
        for (var i=0; i < potentialHypernymsJSON.length; i++) {
            for (var j=0; j < potentialHypernymsJSON[i].length; j++) {
                if (potentialHypernymsJSON[i][j].pointer.relationGroup == 'HYPERNYM') {
                    if (IDs.length <= this.maxNumberSyns) {
                        var currentID = potentialHypernymsJSON[i][j].target;
                        IDs.push(currentID);
                    }
                }
            }
        }
        return IDs;
    }

    extractIDsFromSynset(synsetJSON) {
        var IDs = [];
        for (var i=0; i < synsetJSON.length; i++) {
            if (IDs.length <= this.maxNumberSyns) {
                IDs.push(synsetJSON[i].id);
            }   
        }
        return IDs;
    }

    extractFullLemmasFromSenses(sensesJSON) {
        var fullLemmas = [];
        var ids = [];
        for (var i=0; i < sensesJSON.length; i++) {
            for (var j=0; j < sensesJSON[i].length; j++) {
                if (fullLemmas.length < this.maxNumberSyns) {
                    var currentLemma = sensesJSON[i][j].properties.fullLemma;
                    var currentID = sensesJSON[i][j].properties.synsetID.id;
                    var cleanCurrentLemma = lemmaExtraction.cleanUp(currentLemma);
                    fullLemmas.push(cleanCurrentLemma);
                    ids.push(currentID);
                }
            }
        }
        fullLemmas = this.removeDuplicates(fullLemmas);  // remove duplicates
        fullLemmas = lemmaExtraction.cleanUpArray(fullLemmas);
        return {
            'fullLemmas': fullLemmas,
            'IDs': ids
        };
    }

    getSynsetSenses(synsetIDs) {
        var senses = [];
        for (var i=0; i < synsetIDs.length; i++) {
            // construct URL
            var queryURL = 'https://babelnet.io/v6/getSynset?id=' + synsetIDs[i] + '&key=' + this.key;
            // request senses JSON object for this synset ID
            var httpRes = this.runHttpRequest(queryURL);
            var sensesJSON = JSON.parse(httpRes);
            sensesJSON = sensesJSON.senses;
            senses.push(sensesJSON);
        }
        return senses;  // returns a list of JSON objects corresponding to the senses of each ID of the synset
    }

    getTheme() {
        if (this.themeHasBeenSet == false) {
            this.runFullJob('Theme');
        }
        return this.theme;
    }

    getSubcategory() {
        if (this.subcategoryHasBeenSet == false) {
            this.runFullJob('Subcategory');
        }
        return this.subcategory;
    }

    setTheme(theme) {
        this.theme = theme;
        this.themeHasBeenSet = true;
    }

    setSubcategory(subcategory) {
        this.subcategory = subcategory;
        this.subcategoryHasBeenSet = true;
    }

    runFullJob(classToReturn) {

        var themes = '';
        var subcats = '';

        // get synsets for each lemma in the file name
        for (var i=0; i < this.dataNames.length; i++) {

            // 1. Get parameters for initial Babelnet request
            var initialParams = this.getInitialBabelnetParams(i);

            // 2. Get the initial Synset as JSON object and extract the IDs in it
            var initialSynsetJSON = this.getSynset(initialParams);
            var initialSynsetIDs = this.extractIDsFromSynset(initialSynsetJSON);

            // 3. Get the senses as JSON object and extract the IDs in it,
            // then extract the ('fullLemma') lemmas from each ID.
            // These can be used for subcategory, because they are really close to the actual topic (synonyms).
            var initialSenses = this.getSynsetSenses(initialSynsetIDs);
            var subcategoryResult = this.extractFullLemmasFromSenses(initialSenses);
            var fullLemmas = subcategoryResult.fullLemmas;
            var subcategoryIDs = subcategoryResult.IDs;     // IDs corresponding to the lemmas
            //this.setSubcategory(fullLemmas);
            subcats += fullLemmas;
            if (i != this.dataNames.length-1) {
                if (fullLemmas != '') {
                    if (fullLemmas != "") {
                        subcats += ', ';
                    }
                }
            }

            // Theme will be inferred from the hypernyms.
            // 4. Find and filter potential hypernyms for the subcategory synset
            // (Filter because not all lemmas Babelnet returns have the tag 'hypernym')
            var hypernyms = this.getHypernyms(subcategoryIDs);
            var hypernymIDs = this.extractIDsFromHypernyms(hypernyms);

            // 5. Get the senses of each hypernym
            var hypernymSenses = this.getSynsetSenses(hypernymIDs);
            var themeResult = this.extractFullLemmasFromSenses(hypernymSenses);

            // 6. Exctract the lemmas of the synset entries
            var hypernymLemmas = themeResult.fullLemmas;
            //this.setTheme(hypernymLemmas);
            themes += hypernymLemmas;
            if (i != this.dataNames.length - 1) {
                if (hypernymLemmas != "") {
                    themes += ', ';
                }
            }

        }

        // all lemmas done
        this.setSubcategory(subcats);
        this.setTheme(themes);
        
        // Return the class that was asked for
        if (classToReturn == 'Theme') {
            return this.getTheme();
        } else if (classToReturn == 'Subcategory') {
            return this.getSubcategory();
        } else {
            return null;
        }
    }

}

// RUNTIME TESTS
/*
//var adapter = new BabelNetAdapter('Latest India Status.csv', ['duration', 'quality']);
var adapter = new BabelNetAdapter('Messdaten Anlage Drucklufterzeugung.csv', ["Date (UTC)","Außentemperatur und Feuchtigkeit (100km) [°C] [216956]","Außentemperatur und Feuchtigkeit (100km) [%] [216956]","Druckluftfluss [l/h] [216957]","Kompressor 1 [W] [216958]","Kompressor 3 [W] [216959]"]);
//adapter.runFullJob(); // only necessary if runFullJob is not called by the constructor
console.log("-------");
console.log("Theme(s): " + adapter.getTheme());
console.log("-------");
console.log("Subcategories: " + adapter.getSubcategory());
console.log("-------");
//
*/

module.exports = BabelNetAdapter;
