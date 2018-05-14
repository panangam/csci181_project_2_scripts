// By Simon Lydell 2014.
// This file is in the public domain.

// Returns tuples of the keys and values of `obj`.
exports.objectToArray = function objectToArray(obj) {
  return Object.keys(obj).map(function(key) {
    return [key, obj[key]]
  })
}

// Sorts the tuples of `tuples` in descending order based on the values, and if
// they’re equal, in alphabetical order based on the keys.
exports.sortTuples = function sortTuples(tuples) {
  return tuples.sort(function(tupleA, tupleB) {
    return exports.descending(tupleA[1], tupleB[1]) ||
           exports.alphabetically(tupleA[0], tupleB[0])
  })
}

// Sorts in descending order.
exports.descending = function descending(a, b) {
  return b - a
}

// Sorts in alphabetical order.
exports.alphabetically = function alphabetically(a, b) {
  return a < b ? -1 : a > b ? 1 : 0
}

// Shorthand for incrementing a counter on an object, where you don’t have to
// think about initializing the counter first.
exports.increment = function increment(obj, prop) {
  if (!(prop in obj)) {
    obj[prop] = 0
  }
  obj[prop]++
}

// Returns `string` reversed.
exports.reversed = function reversed(string) {
  return string.split("").reverse().join("")
}

// Returns the key of `tuple`. Useful with `tuples.map(key)`.
exports.key = function value(tuple) {
  return tuple[0]
}

// Returns the value of `tuple`. Useful with `tuples.map(value)`.
exports.value = function value(tuple) {
  return tuple[1]
}

// Sums the values of `tuples`.
exports.sumTuples = function sumTuples(tuples) {
  return tuples
    .map(exports.value)
    .reduce(function(sum, count) {
      return sum + count
    })
}
