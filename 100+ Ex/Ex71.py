#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:04:17 2019

@author: tikilia
"""

import random

print(random.choice([i for i in range(19,150) if i%5==0 and i%7==0]))