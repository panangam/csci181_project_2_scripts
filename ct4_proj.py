# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:35:10 2018

@author: Panangam
"""

from ct_io import ct4
from cribdragging import batchCribDrag, testPos, batchCribDragRange
from util import filterText
import logging

def getGramsFromFile(filename, gram_length, withPeriod=False):
  fin = open(filename, encoding='utf-8', errors='ignore')
  filtered_text = filterText(fin.read(), withPeriod=withPeriod)
  grams = list(set(' '.join(tup) for tup in ngrams(filtered_text, gram_length)))
  fin.close()
  return grams

gram_length = 1

horseGrams = getGramsFromFile('corpus/sources_of_horses_articles.txt', gram_length)
weddingRingsGrams = getGramsFromFile('corpus/wedding_rings_articles.txt', gram_length)
gaitedHorseGrams = getGramsFromFile('corpus/gaited_horse_articles.txt', gram_length)
romanRingsGrams = getGramsFromFile('corpus/roman_ring_articles.txt', gram_length)

with open('corpus/google-10000-english-no-swears.txt') as fin:
  googleCommonGrams = [line[:-1] for line in fin if len(line)>2]
  
allGrams = list(set(horseGrams+weddingRingsGrams+gaitedHorseGrams+romanRingsGrams))



cribRes = batchCribDragRange(ct4, [gram+' ' for gram in googleCommonGrams], 192, 214)
for thing in cribRes[:50]:
  print(thing)

'''
testPosRes = testPos(ct4, 320, (gram+' ' for gram in googleCommonGrams))
for thing in testPosRes[:50]:
  print(thing)
'''
'''
cribResManual = batchCribDragRange(ct4, ['est '], 545, 566)
for thing in cribResManual[:50]:
  print(thing)
'''
