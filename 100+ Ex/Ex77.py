#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:20:49 2019

@author: tikilia
"""

import timeit
code_test='a=1+1'

time=timeit.timeit(code_test,number=100)
print(time)