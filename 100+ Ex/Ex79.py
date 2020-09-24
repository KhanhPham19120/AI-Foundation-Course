#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:16:47 2019

@author: tikilia
"""

subject=['I','YOU']
verb=['PLAY','LOVE']
objects=['HOCKEY','FOOTBALL']

for s in subject:
    for v in verb:
        for o in objects:
            print('{} {} {}'.format(s,v,o))