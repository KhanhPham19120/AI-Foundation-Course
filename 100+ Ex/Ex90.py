#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:55:50 2019

@author: tikilia
"""

import string

n='abcdefga'

for i in string.ascii_lowercase:
    count=n.count(i)
    if count>0:
        print('{}:{}'.format(i,count))