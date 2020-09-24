#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:55:02 2019

@author: tikilia
"""

class CustomException(Exception):
    def __init__(self,mess):
        self.mess=mess

n=int(input())

try:
    if n<10:
        raise CustomException("The number is less than 10!")
    elif n>10:
        raise CustomException('The number is higher than 10')
except CustomException as ce:
    print('Error raised '+ce.mess)
            