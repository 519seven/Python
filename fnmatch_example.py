#!/usr/bin/env python

''' Example demonstrating directory list of files matching a pattern similar to BASH glob '''

import os
import fnmatch

pattern = '*.py'

files = os.listdir('.')
for name in files:
  print ('Filename ({:<25}) matches pattern ({})? {}'.format(name, pattern, fnmatch.fnmatch(name, pattern)))
