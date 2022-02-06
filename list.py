# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:57:08 2022

@author: LENOVO
"""
#Methods of List

#count()
fruit=["apple","orange","bannana","apple"]
x=fruit.count("apple")
print(x)

#append()
flowers=["daisy","lotus","rose"]
flowers.append("lilly")
print(flowers)

#clear()
colors=["Red","Blue","Green","black"]
colors.clear()
print(colors)

#copy()
animals=["Lion","Tiger","Elephant",]
animals.copy()
print(animals)

#extend()
birds=["parrot","crow","peigeon"]
aquatic=["turtel","whale","dolfin"]
birds.extend(aquatic)
print(birds)

#index()
aquatic=["shark","octopus","sea horse"]
x=aquatic.index("octopus")
print(x)

#insert()
vowels=["a","i","o","u"]
vowels.insert(1,"e")
print(vowels)

#pop()
animals=["girraffe","zebra","cow","deer"]
animals.pop(2)
print(animals)

#remove()
animals=["girraffe","zebra","cow","deer"]
animals.remove("cow")
print(animals)

#reverse()
names=["zaffir","ram","ammu"]
names.reverse()
print(names)

#sort()
shapes=["rectangle","square","triangle","circle"]
shapes.sort()
print(shapes)


