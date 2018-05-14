# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:15:59 2018

@author: Panangam
"""

from ct_io import encode_es, decode_es, readProjectTwoCTFile
from ct_io import ct2, ct3
from ngram_util import bigramfreq, trigramfreq, getTrigramProb, getBigramProb

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
      likelihood = getTrigramProb(xor_product_str)
      res.append((word, xor_product_str, likelihood))
  
  res.sort(key=lambda tup: tup[2], reverse=True)
  
  return res

posList = []
keywordList = [
    'corn',
    'cotton',
    'coffee',
    'precious',
    'metal',
    'copper',
    'silver',
    'platinum',
    'sold',
    'sell',
    'bought',
    'buy',
    'raw',
    'valuable',
    'energy','oil','gas',
    'livestock','meat','cattle','republicans',
    'trading','tariff'
    ]

politicskeyword = ['Petty','democrat','republican','independent','liberty','democracy','politician','partisan','legislation','law']
politicsres = []

generic = ['men','they','them','otherwise','but','is','am','are','spoke','history']
genericres = []

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
    for i, crib in enumerate(cribDragging1(ct, ' '+word)):
      if not any([x in crib for x in ['1','2','3','4','  ','..',' .']]):
        # get freq sum
        freqsum = getBigramProb(crib)
        if freqsum > 0:
            res.append((word, i+2, crib, freqsum))
        
  return res

def batchCribDragTrigram(ct, word_list):
  res = []
  
  for word in word_list:
    for i, crib in enumerate(cribDragging1(ct, ' '+word)):
      if not any([x in crib for x in ['1','2','3','4','  ','..',' .']]):
        # get freq sum
        freqsum = getTrigramProb(crib)
        if freqsum > 0:
            res.append((word, i+2, crib, freqsum))
        
  return res

for word in keywordList:
  posList.append([])
  for i, crib in enumerate(cribDragging1(ct2, ' '+word+' ')):
    if not any([x in crib for x in ['1','2','3','4']]):
      posList[-1].append((word, ''+str(i+1)+':'+crib))
      
for word in politicskeyword:
  politicsres.append([])
  for i, crib in enumerate(cribDragging1(ct2, ' '+word+' ')):
    if not any([x in crib for x in ['1','2','3','4']]):
      politicsres[-1].append((word, ''+str(i+1)+':'+crib))
      
for word in generic:
  genericres.append([])
  for i, crib in enumerate(cribDragging1(ct3, ' '+'the law'+' ')):
    if not any([x in crib for x in ['1','2','3','4']]):
      genericres[-1].append((word, ''+str(i+1)+':'+crib))
      

if __name__ == '__main___':
  
  with open('5000words.txt') as wordfile:
    res1 = batchCribDrag(ct3, (line[:-1] for line in wordfile))
    res1 = sorted(res1, key=lambda tup: tup[3], reverse=True)
    for thing in res1[:50]:
      print(thing)
      
  '''
  with open('t_starting.txt') as wordfile:
    words = (line[:-1] for line in wordfile)
    with open('res1.txt', 'w') as outfile:
      for thing in testPos(ct2, 56, words):
        outfile.write(str(thing)+'\n')
        print(thing[1])
  '''