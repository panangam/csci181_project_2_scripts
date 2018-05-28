# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:00:28 2018

@author: Panangam
"""

from ngram_corpus import getNgramFreqDict, getNgramFreqTree
from ct_io import ct1, ct2, ct3, ct4, encode_es, decode_es, c_encode_es, c_decode_es
import numpy as np
from numpy import log, inf, isneginf
import logging
import re

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

trigramTree = getNgramFreqTree(3)

# work on just ct3
ct = ct3
stateCount = len(charset)
obsCount = len(ct)

print('ct length:', obsCount)

# transition is n-gram
# emission is deterministic => 1 or 0 based on printable or not

T1 = np.zeros(shape=(stateCount, obsCount))   # store probability of the most likely path so far
T2 = np.zeros(shape=(stateCount, obsCount), dtype='uint32') # store previous most likely state in the path

# initialize matrices with first n letters
print('j: 0')
for i in range(stateCount):
  T1[i,0] = unigram[charset[i]]
  T2[i,0] = 0
  
print('j: 1')
for i in range(stateCount):
  # get transition probabilities
  probs = []
  for k in range(stateCount):
    str1 = decode_es([k, i])
    str2 = decode_es([k^ct[0], i^ct[1]])
    if str1 not in bigram or str2 not in bigram:
      prob = -inf
    else:
      prob = log(T1[k, 0]) + \
             log(bigram[str1]/unigram[str1[0]]) + \
             log(bigram[str2]/unigram[str2[0]]) 
    probs.append(prob)
  T1[i,1] = max(probs)
  if isneginf(T1[i,1]):
    logger.debug('Got -inf prob at j: %d, str1: %s, str2: %s' % (1, str1, str2))
  T2[i,1] = int(np.array(probs).argmax())
    

for j in range(2, obsCount):
  print('j:', j)
  for i in range(stateCount):
    # get transition probabilities
    probs = []
    str1List = []
    str2List = []
    for k in range(stateCount):
      str1 = decode_es([T2[k,j-1], k, i])
      str2 = decode_es([T2[k,j-1]^ct[j-2], k^ct[j-1], i^ct[j]])
      str1List.append(str1)
      str2List.append(str2)
      
      if str1 not in trigram or str2 not in trigram or re.search('[1234]', str2):
        prob = -inf
      else:
        prob = log(T1[k, j-1]) + \
               log(trigram[str1]/bigram[str1[:-1]]) + \
               log(trigram[str2]/bigram[str2[:-1]])
      probs.append(prob)
    T1[i,j] = max(probs)
    T2[i,j] = int(np.array(probs).argmax())
    if isneginf(T1[i,j]):
      print(str1List)
      logger.error('Got -inf prob at j: %d, i: %d, str1: %s, str2: %s' % (j, i, str1List[T2[i,j]], str2List[T2[i,j]]))
    
# backtrack
print('Backtracking...')
z = [0 for i in range(obsCount)]
X = ['' for i in range(obsCount)]
z[-1] = int(T1[:,-1].argmax())
X[-1] = charset[z[-1]]

for i in reversed(range(1, obsCount)):
  z[i-1] = T2[z[i],i]
  X[i-1] = charset[z[i-1]]
  
print(X)