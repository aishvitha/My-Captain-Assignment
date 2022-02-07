# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:48:24 2022

@author: LENOVO
"""

# Program to display the Fibonacci sequence 

n = int(input("enter the number of sequence "))
n1, n2 = 0, 1
count = 0
if n<= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1   
