# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:51:39 2018

@author: Panangam
"""

from ct_io import ct1, ct2, ct3, ct4
from test1 import batchCribDrag, batchCribDragTrigram, testPos


sexword = [
    'sex',
    'minor',
    'cheat',
    'office',
    'president',
    'kennedy',
    'allege',
    'public',
    'sexual',
    'affair',
    'clinton',
    'offense'
    ]

with open('google-10000-english-no-swears.txt') as wordfile:
  words = (line[:-1].lower() for line in wordfile)
  res1 = batchCribDragTrigram(ct3, words)
  res1 = sorted(res1, key=lambda tup: tup[3], reverse=True)
  for thing in res1[50:50+50]:
    print(thing)