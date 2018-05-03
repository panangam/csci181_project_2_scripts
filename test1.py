# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:15:59 2018

@author: Panangam
"""

from ct_io import encode_es, decode_es, readProjectTwoCTFile
from ct_io import ct2, ct3

def cribDragging1(ct, keyword):
  wordlist = encode_es(keyword)
  ctlist = []
  for i in range(len(ct)-len(wordlist)):
    ct2 = []
    for j, c in enumerate(wordlist):
      ct2.append(ct[i+j]^c)
    ctlist.append(ct2)
    
  return [decode_es(ct) for ct in ctlist]

print(cribDragging1(ct2, 'republic'))