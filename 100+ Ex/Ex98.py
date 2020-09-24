#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:54:09 2019

@author: tikilia
"""

import calendar

month,day,year=map(int,input().split())

dayID=calendar.weekday(year,month,day)

print(calendar.day_name[dayID].upper())