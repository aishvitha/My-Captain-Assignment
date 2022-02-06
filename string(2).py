# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:38:20 2022

@author: LENOVO
"""

#Methods of Strings

#capitalize()
txt="i love python"
x=txt.capitalize()
print(x)

#casefold()
txt="Welcome to My Captain"
x=txt.casefold()
print(x)

#center()
txt="Welcome Have a Great Day"
x=txt.center(50)
print(x)

#count()
txt="I Love Coding, Coding is very interesting"
x=txt.count("Coding")
print(x)

#encode()
txt="My Name is Ståle"
x=txt.encode()
print(x)

#endswith()
txt="Hello,I am from India."
x=txt.endswith(",")
print(x)

#expandtabs()
txt="H\te\tl\tl\to"
x=txt.expandtabs(3)
print(x)

#find()
txt="I love Cooking"
x=txt.find("Cooking")
print(x)

#format()
txt = "For only {price:.8f} dollars!"
print(txt.format(price = 50))

#index()
txt = "Hello, welcome to my world."
x=txt.index("world")
print(x)

#isalnum()
txt="gateway2022"
x=txt.isalnum()
print(x)

#isalpha()
txt="Artificalintelligence"
x=txt .isalpha()
print(x)

#isdecimal()
txt="\u0033"
x=txt.isdecimal()
print(x)

#isdigit()
txt="6000"
x=txt.isdigit()
print(x)

#isidentifier()
txt="Friends"
x=txt.isidentifier()
print(x)

#islower()
txt="hello world"
x=txt.islower()
print(x)

#isnumeric()
txt="1000"
x=txt.isnumeric()
print(x)

#isprintable()
txt="the roman emipire in the era"
x=txt.isprintable()
print(x)

#isspace()
txt="Codingiseasyifweunderstandit"
x=txt.isspace()
print(x)

#istitle()
txt="The Elepanta"
x=txt.istitle()
print(x)

#isupper()
txt="hEllo"
x=txt.isupper()
print(x)

#join()
list=["Rahul","Dhoni","Virat"]
x="@".join(list)
print(x)

#ljust()
txt="Python"
x=txt.ljust(30)
print(x,"is a Coding Language")

#lower()
txt="MUSIC"
x=txt.lower()
print(x)

#lstrip()
txt=" Python "
x=txt.lstrip()
print("of all programming languages",x,"is easy")

#maketrans()
txt="River Panga"
mytable=txt.maketrans("P","G")
print(txt.translate(mytable))

#partition()
txt="Can any Living beings live without oxygen"
x=txt.partition("Living beings")
print(x)

#replace()
txt="I Love Icecreams"
x=txt.replace("Icecreams","Chocolates")
print(x)

#rfind()
txt="Life is full of Suprising,Suprising makes life"
x=txt.rfind("Suprising")
print(x)

#rindex()
txt="My Life, My Rule"
x=txt.rindex("My")
print(x)

#rjust()
txt="Lion"
x=txt.rjust(20)
print(x,"is the king of the jungle")

#rpartition()
txt="I  listen to music everyday, music is my favourite"
x=txt.rpartition("music")
print(x)

#rsplit()
txt="apple,cherry,grapes"
x=txt.rsplit(",")
print(x)

#rstrip()
txt="  Mango "
x=txt.rstrip()
print("of all fruits",x,"is my fav")

#split()
txt="Welcome to My Captain Happy Learning"
x=txt.split()
print(x)

#splitlines()
txt="Thankyou for visting the website\nHope you are satisfied"
x=txt.splitlines()
print(x)

#startswith()
txt="Hello, Welcome to the website."
x=txt.startswith("Hello")
print(x)

#strip()
txt=" Papaya"
x=txt.strip()
print("of all fruit",x,"is my fav")

#swapcase()
txt="I understand French"
x=txt.swapcase()
print(x)

#title()
txt="Welcome to scary land"
x=txt.title()
print(x)

#translate()

mydict={83:  80}
txt="Hello Sam"
print(txt.translate(mydict))

#upper()
txt="hello friends"
x=txt.upper()
print(x)

#zfill()
txt="10"
x=txt.zfill(10)
print(x)


     

