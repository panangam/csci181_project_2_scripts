# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:55:23 2018

@author: Panangam
b"""

charlist = 'abcdefghijklmnopqrstuvwxyz. 1234'

def readProjectTwoCTFile(filename):
    ct_list = []
    ct_list_temp = []
    
    with open(filename) as fin:
        for line in fin:
            if len(line) > 2 and line[1] == '.':
                if len(ct_list_temp) > 0:
                    ct_list.append(ct_list_temp)
                ct_list_temp = []
            elif line[0] == '0' or line[0] == '1':
                ct_raw = line
                ct_raw_list = ct_raw.split(' ')
                ct_raw_list = [c.strip() for c in ct_raw_list if c.strip() != '']
                ct_list_temp += ([int(c, 2) for c in ct_raw_list])
                
    if len(ct_list_temp) > 0:
        ct_list.append(ct_list_temp)
                
    return ct_list
  
def decode_es(ct):
  return ''.join([charlist[ctchar] for ctchar in ct])

def encode_es(pt):
  return [charlist.find(character) for character in pt]

ct_list = readProjectTwoCTFile('ct1.txt')
ct1 = ct_list[0]
ct2 = ct_list[1]
ct3 = ct_list[2]
ct4 = ct_list[3]
    

if __name__ == '__main__':
    ct_list = readProjectTwoCTFile('ct1.txt')
    
    print(len(ct_list), 'ct')
    
    for ct in ct_list:
        print('length:', len(ct))
        
    for ct in ct_list:
        print(ct)
        
    print(decode_es(ct_list[2]))
    print(encode_es('overnight'))