# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 11:41:58 2022

@author: LENOVO
"""
#assignment 2.1

#range()
for x in range(2, 30, 2):
  print(x) 

#infinte()
we cannot make a for loop infinite


#Converting tuple to a list

my_tuple=("red","blue","brown")
s=list(my_tuple)
s.append("green")
my_tuple=tuple(s)
print(my_tuple)

#Add tuple to a tuple

my_tuple=("red","blue","brown")
s=("black",)
my_tuple= my_tuple +s
print(my_tuple)
