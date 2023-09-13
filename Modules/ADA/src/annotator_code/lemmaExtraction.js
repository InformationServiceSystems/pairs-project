// This file contains functions for extracting target lemmas that can be entered on BabelNet to obtain theme(s) and subcategories.

const specialWordsEN = ['of', 'for'];
const specialWordsDE = ['von', 'für', 'zur'];
const specialWords = specialWordsEN.concat(specialWordsDE);

function getTargetLemmas(fileName) {
    var targetLemmas = [];

    if (containsSpecialWords(fileName)) {
        targetLemmas = [formExpression(getLemmas(splitOnSpecialWords(removeFileExtension(fileName)))).trim()]; // return this to use keyword detection
    }
    else {
        targetLemmas = getLemmas(removeFileExtension(fileName));
    }

    return targetLemmas;
}

function containsSpecialWords(str) {
    var contains = false;
    for (var i=0; i<specialWords.length; i++) {
        if (str.includes(specialWords[i])) {
            contains = true;
        }
    }
    return contains;
}

function removeFileExtension(fileName) {

    // Checks if transmitted input filename has extension in it or not and if yes, remove it
    // The file name is split after the _first_ dot
    // Example: "orange.csv.pdf" -> "orange"

    var fileNoExtension = fileName.split('.')[0];   // get everything without extension

    return fileNoExtension;
}


function splitOnSpecialWords(fileName) {

    // Splits a string into the parts separated by special keywords, e.g., prepositions

    var newSplitList = fileName;

    for (var i=0; i < specialWords.length; i++) {
        if (fileName.includes(specialWords[i])) {
            newSplitList = newSplitList.split(specialWords[i]).pop();   // newSplitList contains the part of the file name following a special word
        }
    }

    return newSplitList;
}


function removeDuplicates(array_) {
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


function getLemmas(fileName) {
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
    var noDuplicates = removeDuplicates(noDashes);

    return noDuplicates;
}


function formExpression(lemmas) {
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


function cleanUp(str) {
    var newStr = str;
    while (newStr.includes("_")) {
        newStr = newStr.replace("_", " ");
    }

    newStr = newStr.charAt(0).toUpperCase() + newStr.slice(1);

    return newStr;
}

function cleanUpArray(arr) {

    newArr = "";

    for (var i=0; i<arr.length; i++) {
        if (arr[i] != '') {
            if (i != arr.length-1) {
                newArr += arr[i] + ", ";
            }
            else {
                newArr += arr[i];
            }
        }
    }

    return newArr;

}


module.exports = {getTargetLemmas, cleanUp, cleanUpArray};
