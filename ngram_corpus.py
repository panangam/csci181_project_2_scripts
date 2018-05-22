# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:51:13 2018

@author: Panangam
"""

from ct_io import c_encode_es, c_decode_es
from util import Vividict

import logging
from nltk.corpus import gutenberg
from nltk.util import ngrams
import re
import json
import pickle
import numbers


logger = logging.getLogger('__name__')
corporaList = [gutenberg.raw()]

# n-agnostic ngram frequency tree
# implemented using a Vividict
# accessed
class NgramTree(Vividict):
  def addUp(self):
    if not isinstance(self['f'], numbers.Number): 
      self['f'] = 0
      for branchKey in self:
        if branchKey != 'f':
          self['f'] += self[branchKey].addUp()
    return self['f']
      
  def divideAllWith(self, val):
    self['f'] = self['f']/val
    for branchKey in self:
      if branchKey != 'f':
        self[branchKey].divideAllWith(val)
        
  def normalize(self):
    self.divideAllWith(self['f'])
    
  def addGram(self, gram):
    branch = self
    for c in gram:
      branch = branch[c_encode_es(c)]
    if not isinstance(branch['f'], numbers.Number):
      branch['f'] = 1
    else:
      branch['f'] += 1
      
  def getGramFreq(self, gram):
    branch = self
    for c in gram:
      branch = branch[c_encode_es(c)]
    if not isinstance(branch['f'], numbers.Number):
      branch['f'] = 0
      return branch['f']
    else:
      return branch['f']

# using just gutenberg for now
def getNgramFreqTree(n, retrain=False):
  filename = 'data/%dgram_tree.pickle'%n
  if not retrain:
    try:
      with open(filename, 'rb') as fin:
        print('Trained frequency for n=%d found; Reading data...'%n)
        ngramtree = pickle.load(fin)
      return ngramtree
    except FileNotFoundError:
      pass
    
  print('Training frequency tree for n=%d...'%n)
  
  ngramtree = NgramTree()

  corpus = gutenberg.raw()
  corpus = re.sub('[^a-z. ]',' ', corpus.lower()) 
  corpus = ' '.join(corpus.split())
  corpus_ngram = ngrams(corpus, n)
  
  
  for gram in corpus_ngram:
    ngramtree.addGram(gram)
    
  ngramtree.addUp()
  ngramtree.normalize()
  
  with open(filename, 'wb') as fout:
    pickle.dump(ngramtree, fout)
    
  return ngramtree


# get n-gram frequency from a corpus
# use string as dictionary index
# assume character set of a-z, [period], and [space]
# using just gutenberg corpus
def getNgramFreqDict(n, retrain=False):
  if not retrain:
    try:
      with open('data/%dgram_freq.json'%n) as fin:
        print('Trained frequency for n=%d found; Reading data...'%n)
        ngram_freq = json.load(fin)
      return ngram_freq
    except FileNotFoundError:
      pass
    
  print('Training frequency for n=%d...'%n)
  
  # using whole gutenberg corpus
  corpus = gutenberg.raw()
  corpus = re.sub('[^a-z. ]',' ', corpus.lower()) 
  corpus = ' '.join(corpus.split())
  corpus_ngram = ngrams(corpus, n)
  
  ngram_freq = {}
  
  for gram in corpus_ngram:
    key = ''.join(gram)
    if key in ngram_freq:
      ngram_freq[key] += 1
    else:
      ngram_freq[key] = 1
      
  sum_count = sum([tup[1] for tup in ngram_freq.items()]) 
  for k in ngram_freq.keys():
    ngram_freq[k] = ngram_freq[k]/sum_count
  
  with open('data/%dgram_freq.json'%n, 'w') as fout:
    json.dump(ngram_freq, fout)
    
  return ngram_freq
  
if __name__ == '__main__':
  ngramtree = NgramTree()
  ngramtree.addGram('abc')
  ngramtree.addGram('abb')
  ngramtree.addUp()
  ngramtree.normalize()
  print(ngramtree)
  
  trigramTree = getNgramFreqTree(3, retrain=False)
  print(trigram)