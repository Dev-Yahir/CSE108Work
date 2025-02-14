print("\n -------------------Printing to the Console------------------------------ \n")
def printHello(firstname = "Yahir", lastname = "Mota"):
    print("Hello %s %s " % (firstname, lastname))

#if name is None:
# print("Hello")
#else:
# print("Hello %s" % name)
# the % are not necessary, but can be used for concatenation of strings

printHello()
"""
with open("file.txt", "r") as file:
    myFileContents = file.read()
    can do --> myFileContents += "\nProgramming is fun" --> to add to the file
    file.write(myFilecontents)

reads the whole thing and prints it all out

import os 

os.path.exists("file.txt") --> returns true or false if the file exists
    with open("file.txt", "r+") as file:
        \\\runs if it exists///

example code exists in lecture slides but I learn alot better through applying and creating 
my own code


"""
print("\n ------------------------Classes and Objects------------------------- \n")
# ----------------------------------Classes and Objects--------------------------------------------


class NameClass:
    _name = "Yahir"
    def say_name(self):
        print("Hello, my name is %s" %self._name)

namer = NameClass()
namer.say_name()

#namer._name
# double underscore --> shouldnt access it
# single underscore --> can access it but shouldnt

class Fruit:
    #similiar to a default constructor
    def __init__(self, color, numSeeds):
        self.color = color
        self.numSeeds = numSeeds

    def printInfo(self):
        print("Color", self.color, "\nNumber of seeds", self.numSeeds)

print("Apple")
apple = Fruit("Red", 10)
apple.printInfo()

print("Orange")
orange = Fruit("Orange", 0)
orange.printInfo()

"""
object --> instance of a class
a class that has been instantiated
no values in it

class --> blueprint for objects

self is a reference to the instance(object) of the class
"""
print("\n --------------------Inheritence----------------------------- \n")
#----------------------------------Inheritance--------------------------------------------
# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class

class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printname(self):
        print("Name: ", self.firstname, " ", self.lastname, "\nAge: ", self.age)

# Child class is the class that inherits from another class, also called derived class

class Student(Person):
    def __init__(self, fname, lname, age, gradYear):
        super().__init__(fname, lname, age)
        self.gradYear = gradYear

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.gradYear)

me = Student("Yahir", "Mota", 20, 2025)

me.welcome() # this prints out the welcome message

print("\n -------------------Dictionaries------------------------------ \n")
#----------------------------------Dictionaries------------------------------------------
# Dictionaries are used to store data values in key:value pairs
# Based on a Hash table it is a very efficient data sctructure
# emptyDict = {}
# can store any type of data

grades = {'Math': 90, 'Science': 85, 'English': 95}

print(grades['Math'])
print(grades.keys())
print(list(grades.keys()))
print(grades.values())
print(list(grades.values()))
print(grades.items())
print(list(grades.items()))

#it is possible to nest dictionaries within dictionaries

print("\n -------------------JSON------------------------------ \n")
#----------------------------------JSON------------------------------------------
#Python has a built-in package called json, which can be used to work with JSON data

import json

names_json = """{"john": "doe", "smith": "jane"}"""
names_dict = json.loads(names_json)
print(names_dict)
"""
with open('data.json') as json_file:
    data = json.load(json_file)
    print(data)
"""

#----------------------------------Modules------------------------------------------
"""
draw.py file:

def draw_game(result):
    ---code---

def clear_screen(screen):
    ---code---


import draw

def play_game():
    ---code---

if __name__ == "__main__":
    result = play_game()
    draw_game(result)

it is used to run some code from other files
Also can be used to import functions from other files
and can be pretty customizable when importing
"""

#----------------------------------Packages------------------------------------------
"""
a_package
    __init__.py
    module1.py
    module2.py
"""

#ensure to catch up properly on the lecture slides