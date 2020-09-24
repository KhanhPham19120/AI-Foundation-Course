#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:19:11 2019

@author: tikilia
"""

class Car:
    name = "Car"

    def __init__(self,name):
        self.name = name
        
bmw=Car("BMW")
print("{0} name is {1}".format(Car.name,bmw.name))