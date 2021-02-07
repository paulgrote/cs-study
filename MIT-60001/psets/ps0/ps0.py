#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:48:51 2020

@author: paulgrote
"""
import numpy

x = int(input("Please enter number x: "))
y = int(input("Please enter nubmer y: "))
power = x**y
logx = numpy.log2(x)
print("x**y = " + str(power))
print("log(x) = " + str(logx))
