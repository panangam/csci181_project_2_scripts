Overview
========

A bunch of functions to analyse frequencies in text.


Installation
============

`npm install text-frequencies-analysis`


Tuples
======

This collection of functions is all about _tuples._ Here, a tuple means an array
with two items. The first item is a string, and the second one a number—the
frequency of the string. For example, `["a",5]`.

There are two functions—`countEach` and `countPairs`—that return arrays of
tuples. In other words, they _produce_ data.

The rest of the functions let you work with the data.


Usage
=====

Each function is described in the source code. The tests are also informative.

Moreover, the file analyse.js is an example on how to use the tuple-producing
functions. Here’s a [gist] of the output, as an example.

Here’s a small taste of what you can do with the rest of the functions:

`filter` lets you filter an array of tuples. For example, to filter out all
pairs of english letters that contain the letter “e” and another vowel:
from an array of character-tuples:

    filter(pairs, /e/, /[aouiy]/)

`relative` makes frequencies into percentages.

`sumTuples` sums all the frequencies in an array of tuples.

If we wanted to know how many percent the “e+vowel” pairs make out of all pairs,
we could run the following:

    sumTuples(filter(relative(pairs), /e/, /[aouiy]/))

Sometimes it’s hard to believe that a certain pair of letters is as common as
your data say. Then it’s useful to get a list of words that include that pair.

    pairWords(words, "ul")

[gist]: https://gist.github.com/lydell/e807977107e041c147ab


License
=======

All files are in the public domain.
