// By Simon Lydell 2014.
// This file is in the public domain.

var helpers = require("./helpers")

var objectToArray       = helpers.objectToArray
var sortTuples          = helpers.sortTuples
var increment           = helpers.increment
var reversed            = helpers.reversed
var sumTuples           = helpers.sumTuples



// Returns tuples of each string in `array` and its count.
exports.countEach = function countEach(array) {
  var map = Object.create(null)

  array.forEach(increment.bind(null, map))

  return sortTuples(objectToArray(map))
}



// Returns tuples of each pair of characters in `text` and their counts. The
// pair must match `regex`. Two identical characters are not considered a pair.
// The characters in a pair are sorted alphabetically.
exports.countPairs = function pairs(text, regex) {
  var pairMap = Object.create(null)

  text.slice(0, -1).split("").forEach(function(char, index) {
    var nextChar = text[index + 1]
    if (char !== nextChar && regex.test(text.substr(index, 2))) {
      var pair = [char, nextChar].sort().join("")
      increment(pairMap, pair)
    }
  })

  return sortTuples(objectToArray(pairMap))
}



// Returns a comma separated string of each word in `words` that contains
// `pair`, where the pair is highlighted: Every occurrance of the pair
// (forwards or backwards) is uppercase and everything else is lowercase.
exports.pairWords = function pairWords(words, pair) {
  return words
    .filter(function(word) {
      return word.indexOf(pair) >= 0 || word.indexOf(reversed(pair)) >= 0
    })
    .map(highlight.bind(null, pair))
    .join(" ")
}

function highlight(pair, word) {
  return word.split("").map(function(char, index, array) {
    var previousChar = array[index-1]
    var nextChar     = array[index+1]
    if (
      (char === pair[0] && nextChar === pair[1]) ||
      (char === pair[1] && nextChar === pair[0]) ||
      (char === pair[0] && previousChar === pair[1]) ||
      (char === pair[1] && previousChar === pair[0])
    ) {
      return char.toUpperCase()
    }
    return char.toLowerCase()
  }).join("")
}



// Returns tuples of `tuples` whose keys match each regex in `regexes`. Since
// the `g` flag is useless, it is instead used to indicate that a regex should
// _not_ match.
exports.filter = function filter(tuples /*, ...regexes */) {
  var regexes = Array.prototype.slice.call(arguments, 1)
  return tuples.filter(function(tuple) {
    return regexes.reduce(function(ok, regex) {
      if (!ok) {
        return false
      }
      regex.lastIndex = 0
      var test = regex.test(tuple[0])
      var inverted = regex.global
      return inverted ? !test : test
    }, true)
  })
}



// Returns tuples whose values are relative to the sum of the values of
// `tuples`.
exports.relative = function relative(tuples) {
  var sum = sumTuples(tuples)
  return tuples.map(function(tuple) {
    return [tuple[0], tuple[1] / sum * 100]
  })
}



// Expose `sumTuples`.
exports.sumTuples = sumTuples



// Expose `sortTuples`.
exports.sortTuples = sortTuples



// Like `JSON.stringify(array)`, except that each item of `array` is on a new
// row. Useful to stringifiy arrays of tuples in a more readable manner.
exports.jsonStringifyRow = function jsonStringifyRow(array) {
  return [
    "[",
    array.map(JSON.stringify).join(",\n"),
    "]"
  ].join("\n")
}
