# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:39:23 2018

@author: Panangam
"""

from ct_io import ct1, ct3
from ct_io import encode_es, decode_es
from ngram_util import getTrigramProb, getBigramProb
import re

with open('google-10000-english-no-swears.txt') as wordsfile:
  words = (line[:-1] for line in wordsfile)
  res = []
  
  for word in words:
    inv_pt = decode_es([encode_es(c)[0]^ct1[i+11] for i, c in enumerate(word+' ') if len(word)+11<len(ct3)])
    prob = getBigramProb(inv_pt)
    if re.search('[0-9]', inv_pt):
      continue
    if prob <= 0 or inv_pt[0]=='.' or inv_pt[0]==' ': 
      continue
    res.append((word, inv_pt, prob))
      
  res.sort(key=lambda tup: tup[2], reverse=True)
  for thing in res:
    if thing[2] > 0.0001: print(thing)