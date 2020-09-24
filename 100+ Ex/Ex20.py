#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:43:25 2019

@author: tikilia
"""

class test():
    def _init_(self):
        pass
    def generator(self,n):
        return [i for i in range(n+1) if i%7==0]
    
n=int(input())
xx=test()
lst=xx.generator(n)
print(lst)

    