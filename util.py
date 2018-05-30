# -*- coding: utf-8 -*-
"""
Created on Mon May 21 22:16:36 2018

@author: Panangam
"""
import re
import logging

#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

# taken from https://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries
class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup
      
def filterText(text, withPeriod=False):
  text.translate({'\n': ' '})
  if withPeriod:
    filtered_text = (c.lower() for c in text if re.match('[a-z .]', c.lower()))
  else:
    filtered_text = (c.lower() for c in text if re.match('[a-z ]', c.lower()))

  return ''.join(filtered_text).split()
  