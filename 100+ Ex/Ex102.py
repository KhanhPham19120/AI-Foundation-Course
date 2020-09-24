#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:13:58 2019

@author: tikilia
"""

n=input()

digit=0
letter=0

for i in n:
    digit+=i.isdigit()
    letter+=i.isalpha()
    
print('Digit - {}'.format(digit))
print('Letter - {}'.format(letter))