# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:53:58 2022

@author: LENOVO
"""
#print all positive number in a range
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ",nums)
pos_nums = [n for n in nums if n> 0]
print("Positive numbers in the said list: ",pos_nums)
