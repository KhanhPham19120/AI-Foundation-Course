#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:32:50 2019

@author: tikilia
"""
import textwrap

str_S=input()
width_W=int(input())


lst=textwrap.wrap(str_S,width_W)

for i in lst:
    print(i)