#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:04:27 2019

@author: tikilia
"""

def BinarySearch(lst,n,x):
    if len(lst)>0:
        mid=int(n/2)
        
        if x==lst[mid]:
            return mid
        
        if x>lst[mid]:
            for i in range(mid,len(lst)):
                if x==lst[i]:
                    return i
        
        if x<lst[mid]:
            for i in range(0,mid):
                if x==lst[i]:
                    return i
    else:
        return -1
    
n=[2,3,5,1,8,7]
n.sort()
num=7

print(BinarySearch(n,(len(n)-1),num))
    
    