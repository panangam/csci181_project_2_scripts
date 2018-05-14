// By Simon Lydell 2014.
// This file is in the public domain.

var assert = require("assert")

var helpers = require("../lib/helpers")


suite("helpers", function() {

  test("objectToArray", function() {
    assert.deepEqual(
      helpers.objectToArray({
        "bc": 3,
        "ab": 3,
        "cd": 4
      }), [
        ["bc",3],
        ["ab",3],
        ["cd",4]
      ]
    )
  })


  test("sortTuples", function() {
    assert.deepEqual(
      helpers.sortTuples([
        ["bc",3],
        ["ab",3],
        ["cd",4]
      ]), [
        ["cd",4],
        ["ab",3],
        ["bc",3]
      ]
    )
  })


  test("descending", function() {
    assert.deepEqual(
     [1, 3, 2].sort(helpers.descending),
     [3, 2, 1]
    )
  })


  test("alphabetically", function() {
    assert.deepEqual(
     ["c", "a", "b"].sort(helpers.alphabetically),
     ["a", "b", "c"]
    )
  })


  test("increment", function() {
    var obj = {}
    helpers.increment(obj, "foo")
    helpers.increment(obj, "foo")
    helpers.increment(obj, "bar")
    helpers.increment(obj, "foo")
    assert.deepEqual(obj, {
      foo: 3,
      bar: 1
    })
  })


  test("reversed", function() {
    assert.equal(helpers.reversed("abc"), "cba")
  })


  test("key", function() {
    assert.equal(helpers.key(["ab", 3]), "ab")
  })


  test("value", function() {
    assert.equal(helpers.value(["ab", 3]), 3)
  })


  test("sumTuples", function() {
    assert.equal(helpers.sumTuples([[,1], [,2], [,3]]), 6)
  })

})
