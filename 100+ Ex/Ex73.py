#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:08:26 2019

@author: tikilia
"""

import random

print(random.sample([i for i in range(100,201) if i%2==0],5))