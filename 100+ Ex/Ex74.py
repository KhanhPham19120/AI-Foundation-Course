#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:10:08 2019

@author: tikilia
"""

import random

print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))