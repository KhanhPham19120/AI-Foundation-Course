#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:11:09 2019

@author: tikilia
"""
import itertools

lst=[1,2,3]

permutation=itertools.permutations(lst)

for i in permutation:
    print(i)