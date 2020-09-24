#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:15:45 2019

@author: tikilia
"""

import zlib

s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s.encode('utf-8'))

b=zlib.decompress(t)

print(b)