#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:49:02 2019

@author: tikilia
"""

num = input().split(',')
odd = [str(int(i)**2) for i in num if int(i)%2!=0]
print(','.join(odd))