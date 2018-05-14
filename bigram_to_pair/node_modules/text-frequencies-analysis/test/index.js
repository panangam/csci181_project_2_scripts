// By Simon Lydell 2014.
// This file is in the public domain.

var assert = require("assert")

var tools   = require("../lib/index")
var helpers = require("../lib/helpers")


suite("tools", function() {

  test("countEach", function() {
    assert.deepEqual(tools.countEach([
      "b",
      "a",
      ".",
      "word",
      "a", "b", "b", "c", ",", ".", "...", "a",
      "w", "word", "w or d"
    ]), [
      ["a",3],
      ["b",3],
      [".",2],
      ["word",2],
      [",",1],
      ["...",1],
      ["c",1],
      ["w",1],
      ["w or d",1]
    ])
  })


  test("countPairs", function() {
    assert.deepEqual(tools.countPairs("There are three things here.", /^[a-z]{2}$/), [
      ["er",6],
      ["eh",2],
      ["ht",2],
      ["ar",1],
      ["gn",1],
      ["gs",1],
      ["hi",1],
      ["hr",1],
      ["in",1]
    ])
  })


  test("pairWords", function() {
    var words = ["there", "are", "rivers", "in", "reALity"]
    assert.equal(tools.pairWords(words, "ht"), "THere")
    assert.equal(tools.pairWords(words, "er"), "thERE aRE rivERs REality")
    assert.equal(tools.pairWords(words, "re"), "thERE aRE rivERs REality")
    assert.equal(tools.pairWords(words, "AL"), "reALity")
    assert.equal(tools.pairWords(words, "qz"), "")
  })


  test("sumTuples", function() {
    assert.equal(tools.sumTuples, helpers.sumTuples)
  })


  test("sortTuples", function() {
    assert.equal(tools.sortTuples, helpers.sortTuples)
  })


  test("filter", function() {
    var tuples = [
      ["ab",3],
      ["bc",2],
      ["ac",1],
      ["bd",5]
    ]

    assert.deepEqual(tools.filter(tuples), tuples)
    assert.deepEqual(tools.filter(tuples, /a/),  [["ab", 3], ["ac", 1]])
    assert.deepEqual(tools.filter(tuples, /a/g), [["bc", 2], ["bd", 5]])
    assert.deepEqual(tools.filter(tuples, /b/g), [["ac", 1]])
    assert.deepEqual(tools.filter(tuples, /b/, /a/),  [["ab", 3]])
    assert.deepEqual(tools.filter(tuples, /b/, /a/g), [["bc", 2], ["bd", 5]])
    assert.deepEqual(tools.filter(tuples, /b/, /c/g), [["ab", 3], ["bd", 5]])
  })


  test("relative", function() {
    assert.deepEqual(
      tools.relative([
        ["ab",3],
        ["bc",2]
      ]), [
        ["ab",60],
        ["bc",40]
      ]
    )
  })


  test("jsonStringifyRow", function() {
    assert.equal(
      tools.jsonStringifyRow([
        ["a",2],
        ["b",3]
      ]), [
        '[',
        '["a",2],',
        '["b",3]',
        ']'
      ].join("\n")
    )
  })

})
