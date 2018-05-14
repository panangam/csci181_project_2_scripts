# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:02:16 2018

@author: Panangam
"""

import json
import re

# bigram 

bigramfreq = {}

with open('bigram_to_pair/bigrams.json') as bigramfile:
  bigramfreq_list = json.load(bigramfile)
  for (bigram, freq) in bigramfreq_list:
    bigramfreq[bigram] = freq
  
  
freqsum = 0
for bigram, freq in bigramfreq.items():
  freqsum += freq
  
for bigram, freq in bigramfreq.items():
  bigramfreq[bigram] = freq/freqsum
  
# trigram
  
trigramfreq = {}
freqsum = 0

with open('english_trigrams.txt') as trigramfile:
  for line in trigramfile:
    trigramfreq[line[:3].lower()] = int(line[4:-1])
    freqsum += int(line[4:-1])
  
for trigram, freq in trigramfreq.items():
  trigramfreq[trigram] = freq/freqsum
  
def getBigramProb(phrase):
  freqsum = 0
  j = 0
  
  if re.search('[0-9]', phrase): return 0
  
  for k in range(len(phrase)-1):
    if not bigramFilter(phrase[k:k+2]): return 0
    if (phrase[k]!=' ' and phrase[k]!='.' and phrase[k+1]!=' ' and phrase[k+1]!='.'):
      freqsum += bigramfreq[phrase[k:k+2]]
      j += 1
  freqsum /= (j+1)
  return freqsum

def getTrigramProb(phrase):
  freqsum = 0
  j = 0
  
  if re.search('[0-9]', phrase): return 0
  
  for k in range(len(phrase)-2):
    if not trigramFilter(phrase[k:k+3]): return 0
    if ('.' not in phrase[k:k+3] and ' ' not in phrase[k:k+3]):
      if phrase[k:k+3] in trigramfreq:
        freqsum += trigramfreq[phrase[k:k+3]]
      j += 1
  if j != 0: freqsum /= j
  return freqsum

def bigramFilter(t):
  return not ((t[0]=='.' and t[1]!=' '))

def trigramFilter(t):
  return not ((t[0]=='.' and t[2]=='.') or 
             (t[0]=='.' and t[1]!=' ') or
             (t[1]=='.' and t[2]!=' ') or
             (' .' in t) or
             ('..' in t) or 
             ('  ' in t))


if __name__ == '__main__':
  print(bigramfreq)
  print('abcd'[0:2])
  print(len('abcd'))
  print(trigramFilter('a. '))