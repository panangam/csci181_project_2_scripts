// By Simon Lydell 2014.
// This file is in the public domain.

// Example invocation:
//
//     node analyse data/en <text.txt
//
// The above creates three JSON files in the data/en directory: chars.json,
// pairs.json and words.json. They contain, in order, the frequencies of each
// character, each pair of English letters and each English word in text.txt.
//
// To analyse Swedish:
//
//     node analyse data/sv '[a-zåäö]' <text.txt
//

var DIR    = process.argv[2] || "."
var LETTER = process.argv[3] || "[a-z]"

var fs    = require("fs")
var path  = require("path")
var stdin = require("get-stdin")
var tools = require("./")

stdin(function(text) {
  text = text.toLowerCase()

  write("chars.json", tools.countEach(text.split("")))
  write("pairs.json", tools.countPairs(text, RegExp("^" + LETTER + "{2}$", "")))
  write("words.json", tools.countEach(text.match(RegExp(LETTER + "+", "g") || [])))
})

function write(name, tuples) {
  fs.writeFileSync(path.join(DIR, name), tools.jsonStringifyRow(tuples))
}
