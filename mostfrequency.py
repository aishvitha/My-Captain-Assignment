# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:51:30 2022

@author: LENOVO
"""

#Most frequent character
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
    sort(d)

print( most_frequent('fffhhsghehfhjshyt'))