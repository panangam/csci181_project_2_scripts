# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:51:13 2018

@author: Panangam
"""

import logging
from itertools import islice
from nltk.corpus import gutenberg
from nltk.util import ngrams
import re
import json

logger = logging.getLogger('__name__')

corpora_list = []

# get n-gram frequency from a corpus
# assume character set of a-z, [period], and [space]
# using just gutenberg corpus
def getNgramFreq(n, retrain=False):
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
  a = getNgramFreq(6)