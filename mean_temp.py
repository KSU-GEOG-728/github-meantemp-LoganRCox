#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: mean_temp.py
    Author: Logan Cox
    Description:  Calculates mean daily temperature from two user defined variables representing a daily high (x) and low (y) temperature
    Date created: 08/26/24
    Python Version: 3.9.16
"""

# Assign variable x the value for the previous day's high temperature
x = 101

# Assign variable y the value for the previous day's low temperature
y = 74

# Create variable z and use mathematical operators to calculate the mean temperature
z = 2 * (x + y)

# Use this custom statement that prints the result to screen
print("Yesterday's mean daily temperature was {0} degrees.".format(z))
