# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:15:59 2018

@author: Panangam
"""

from ct_io import encode_es, decode_es, readProjectTwoCTFile
from ct_io import ct2, ct3
from ngram_util import bigramfreq, trigramfreq, getTrigramProb, getBigramProb
from ngram_corpus import getNgramFreqTree

from nltk.util import ngrams
import math

ngram_length = 4
ngramtree = getNgramFreqTree(ngram_length)

def cribDragging1(ct, keyword):
  wordlist = encode_es(keyword)
  ctlist = []
  if len(ct) >= len(wordlist):
    for i in range(len(ct)-len(wordlist)):
      ct2 = []
      for j, c in enumerate(wordlist):
        ct2.append(ct[i+j]^c)
      ctlist.append(ct2)
    
  return [decode_es(ct) for ct in ctlist]

def testPos(ct, pos, wordlist):
  res = []
  for word in wordlist:
    word_code = encode_es(word)
    xor_product = [ct[pos+i]^word_pos for i, word_pos in enumerate(word_code)]
    xor_product_str = decode_es(xor_product)
    if not any([x in xor_product_str for x in ['1','2','3','4','  ','..',' .']]):
      prob = ngramtree.evaluateLogProb(xor_product, ngram_length)/(len(xor_product)-ngram_length)
      if prob != -inf and not math.isnan(prob) and prob != 0:
        res.append((word, xor_product_str, prob))
  
  res.sort(key=lambda tup: tup[2], reverse=True)
  
  return res

def getLikelihood(phrase):
  freqsum = 0
  j = 0
  for k in range(len(phrase)-1):
    if (phrase[k]!=' ' and phrase[k]!='.' and phrase[k+1]!=' ' and phrase[k+1]!='.'):
      freqsum += bigramfreq[phrase[k:k+2]]
      j += 1
  freqsum /= (j+1)
  return freqsum

def batchCribDrag(ct, word_list):
  res = []
  
  for word in word_list:
    for i, crib in enumerate(cribDragging1(ct, word)):
      if not any([x in crib for x in ['1','2','3','4']]):
        # get log prob
        prob = ngramtree.evaluateLogProb(crib, ngram_length)/(len(crib)-ngram_length)
        if prob != -inf and not math.isnan(prob) and prob < 0:
            res.append((word, i, crib, prob))
  res.sort(key=lambda tup: tup[3], reverse=True)
  return res

if __name__ == '__main__': 
  '''
  with open('5000words.txt') as wordfile:
    words = (line[:-1] for line in wordfile)
    res1 = testPos(ct1, 88, words)
    res1 = sorted(res1, key=lambda tup: tup[2], reverse=True)
    for thing in res1[:50]:
      print(thing)
  '''
  
  with open('corpus/olympicpool.txt', encoding='utf-8') as fin:
    fulltext = fin.read()
    filtered_text = (c.lower() for c in fulltext if re.match('[a-z ]', c.lower()))
    filtered_text = ''.join(filtered_text).split(' ')
    text_grams = list(set(' '.join(tup) for tup in ngrams(filtered_text, 3)))
    
    '''
    res2 = batchCribDrag(ct1, text_grams)
    res2 = sorted(res2, key=lambda tup: tup[3], reverse=True)
    for thing in res2[:50]:
      print(thing)
    '''
    '''
    res3 = testPos(ct1, 88, text_grams)
    print('test')
    for thing in res3:
      print(thing)
    '''
    res4 = batchCribDrag(ct1[88:276], text_grams)
    for thing in res4[:50]:
      print(thing)
    
    