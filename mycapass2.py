# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:03:25 2022

@author: LENOVO
"""

#Functions

#calling a function
def my_function():
    print("hello world")
my_function()  


#Arguments
def my_function(fname):
    print(fname+"Hello ")
my_function("Ram") 
my_function("Sam")  
my_function("Leo")


#Number of Arguments
def my_function(fname,  hname):
    print(fname+" " +hname)
my_function("Sam","Leo") 


#Arbitrary Arguments(*args)  
def my_function(*color):
    print("The most fav color is" + color[0])
my_function(" Black","lavendar","pink") 


#Keyword Arguments
def my_function(dish1,dish2,dish3):
    print("The most fav food is"+dish1)
my_function(dish1=" Ice cream",dish2="Chocolates",dish3="pastries") 


#Arbitarty keyword Arguments(**kwargs)
def my_function(**Player):
    print("The Indian Cricket Player" +Player["name"])
my_function(fname="Bravo" , name=" Dhoni")  


#Default parameter value
def my_function(country=" Indian"):
    print("I am an" + country)
my_function(" Sweden") 
my_function()
my_function(" US")  


#passing a list as an Arguments
def my_function(food):
    for s in food:
        print(s)
items=["Chapathi", "porotta", "Naan"] 
my_function(items) 


#Return values
def my_function(s):
    return 5*s
print(my_function(2))
print(my_function(4))
print(my_function(6))

#Recursion
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
     result=0
     return result
     print("\n\n Recursion result")
     tri_recursion(6)
     
#Methods of Dictionary

#clear()

car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
car.clear()
print(car)   

#copy()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.copy()
print(s)   


#fromkeys()
s=("key 1","key 2","key 3")
y=0
thisdict=dict.fromkeys(s,y)
print(thisdict)

#get()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.get("model")
print(s) 

#items()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.items()
print(s) 

#keys()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.keys()
print(s) 

#pop()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.pop("model")
print(s) 

#popitem()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.popitem()
print(s) 

#setdefault()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.setdefault("model","Bronco")
print(s) 

#update(){"Brand" : "Ford","mode
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
car.update({"color": "Black"})
print(car)

#values()
car={"Brand" : "Ford","model" : "Mustang","year" :    1964}
s=car.values()
print(s)

#Create a Set()
myset={"Flowers","fruits","vegetables"}
print(myset)

#duplicate values
myset={"Flower","fruits","vegetables","fruits"}
print(myset)

#length of set()
myset={"Flower","fruits","vegetables","fruits"}
print(len(myset))

#set items()
myset1={"Mango","starwberry","Rasberry"}
myset2={"1","2","3"}
myset3={"a","e","i","o","u"}
print(myset1)
print(myset2)
print(myset3)

#type()
myset={"Flowers","fruits","vegetables"}
print(type(myset))


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

#Function of string()
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : "+(f_extns[-1]))

#calculator()
def multiplication(num1, num2):
    return num1 * num2

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 / num2

value1 = int(input("Enter 1st number: "))
value2 = int(input("Enter 2nd number: "))

print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction")
operation = int(input("Choose operation 1/2/3/4: "))

if operation == 1:
    print(value1, "/", value2, "=", divide(value1, value2))
elif operation == 2:
   print(value1, "*", value2, "=", multiplication(value1, value2))

elif operation == 3:
   print(value1, "+", value2, "=", addition(value1, value2))
elif operation == 4:
   print(value1, "-", value2, "=", subtraction(value1, value2))
else:
   print("Enter correct operation")
    

 
   




    
    








 





     
   
  
 

    

