# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:09:40 2018

@author: Panangam
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:35:10 2018

@author: Panangam
"""

from ct_io import ct1
from cribdragging import batchCribDrag, testPos
from util import filterText
import logging

with open('corpus/olympicpool2.txt', encoding='utf-8', errors='ignore') as fin:
  print('===olympic pool===')
  text = fin.read()
  filtered_text = filterText(text, withPeriod=False)
  # print(filtered_text)
  text_grams = list(set(' '.join(tup) for tup in ngrams(filtered_text, 3)))
  print('CT length:', len(ct1))
  print('Grams count:', len(text_grams))
  
  
  cribResOlympic = batchCribDrag(ct1, text_grams)
  for thing in cribResOlympic[:50]:
    print(thing)
  with open('data/cribResCT1Olympic.txt', 'w') as fout:
    for thing in cribResOlympic:
      fout.write(str(thing)+'\n')
  
  '''
  testPosRes = testPos(ct1, 161, text_grams)
  for thing in testPosRes[:50]:
    print(thing)
    pass
  '''
  
with open('corpus/amazon_articles.txt', encoding='utf-8', errors='ignore') as fin:
  print('===amazon and bookstores===')
  text = fin.read()
  filtered_text = filterText(text, withPeriod=False)
  # print(filtered_text)
  text_grams = list(set(' '.join(tup) for tup in ngrams(filtered_text, 3)))
  print('CT length:', len(ct1))
  print('Grams count:', len(text_grams))
  
  '''
  cribResAmazon = batchCribDrag(ct1, text_grams)
  for thing in cribResAmazon[:50]:
    print(thing)
  with open('data/cribResCT1Amazon.txt', 'w') as fout:
    for thing in cribResAmazon:
      fout.write(str(thing)+'\n')
  '''
  
'''
cribResManual = batchCribDrag(ct4, ['middle', 'middle ages', 'copper ages'])
for thing in cribResManual[:50]:
  print(thing)
'''