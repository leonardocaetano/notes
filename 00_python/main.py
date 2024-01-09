# REMEMBER TO DONWLOAD THE COURSE FILES (and put it on desktop k)

# so... python has variables... and also f-strings

# in python a variable is a not a box, but a _label_ (a pointer? a reference?)

first_name = 'ada'
second_name = 'lovelace'

full_name = f"Hey {first_name} {second_name}, you good?"

print(f"Hey {first_name} {second_name}, you good?")
print("Hey {first_name} {second_name}, you good?")
print(full_name.title())
print("\tTab\nNewLine\nNewLine\nNewLine")

#the  .rstrip() removes the extra whitespace from left and right sides

with_prefix = "abc.python"
print(with_prefix.removeprefix('abc.'))

# so... we can see that python has various methods to dealing with strings, stuff like .title(),
# .captilize(), etc... they don't alter the original strings

# the difference between single and double quotes

# single_string = 'This is a 'single' quote string.'
double_string = "This is a 'double' quote string."

# print(single_string)
print(double_string)

# you can use the double quotes when the single quote is likely to be used in a string

# ---- NUMBERS ----

print(2 + 3 * 4) # prints 14
print((2+3) * 4) # prints 20

# python can also deal with floats

print(2 ** 16) # same as 2^16

print(65_536) # this makes numbers more readable

ass1, ass2, ass3 = 321, 23.4, "bruh" #this is how you do multiple assignments

print(ass1)
print(ass2)
print(ass3)

THIS_IS_A_CONSTANT = "Get REAL SKILLZ" #captilize all letters to make it a constant
ass3 = "not_bruh" # since this is not a constant, you can re-assign it

# python has this goofy "zen of python" philosofy, that says things like "avoid complexity" which is good, but
# also says stuff like "beautiful is better then ugly" ???????
# there's also "if two python programmers are asked to solve the same problem, the result should be the same"
# meaning "there should be one -- and preferably --- only one obvious way to do it."

# --- LISTS --- (aka arrays)

steely_dan = ['aja', 'gaucho', 'pretzel_logic'] # the [] is what indicates a list

print(steely_dan[0]) # this is how you access a list, and yes, we start at [0]
print(steely_dan[1])
print(steely_dan[2])
print(steely_dan)    # you can also do this as well, but i guess this depedends on what you are doing

print(steely_dan[0].title()) # you can do this ofc
# print(steely_dan.title()) # but you can't do this

print(steely_dan[-1]) # do have this syntax to access the last element, ofc it prints pretzel_logic

# to append new items to a list, you can just reassign it, repeating all the old elements and adding the new ones

# but you can also append elemets

steely_dan.append('katy_lied') # this will be [3]
steely_dan.append("can't_buy_a_thrill") # and [4]

print(steely_dan) # append doesnt go back in time to apply changes, so you have to reprint if you want to see all

# and we can also pop them

steely_dan.pop()

print(steely_dan) # popping only removes the last item

# if you want to remove a specifc item do

steely_dan.remove('gaucho')

# you can also do this

item_to_remove = 'aja'

steely_dan.remove(item_to_remove) 

print(steely_dan)

# @NOTE: the remove() method only remove the first appearence of a element, you need to use a loop to make sure all elements that are the same is remove

# for last, you can manually change a specific element of the list

steely_dan[0] = 'the_nightfly'

# you can also use the insert and delete with lists, you can also sort them!!!

steely_dan.sort()
print(steely_dan)
steely_dan.sort(reverse=True)
print(steely_dan)

# vim @NOTE: when in visual mode, the cursor position is also selected
# the pasting happens after the cursor, and below!!!

# back to lists: yeah, there's a lot of methods you can apply to it... reverse, sort, len, sorted...
# the difference between sort and sorted is that sorted criates a new list, while sort affects the original

# ---- WORKING WITH LISTS ----

ye = ['cd', 'lr', 'grad', '808s', 'mbdtf', 'yee', 'pablo', 'jik', 'd', 'd2']

# we can now loop!!!!

for record in ye:  # the record variable gets created here
    print(record)

for record in ye:  # well, i guess that it is also impotant to @NOTE that this range is [inclusive]
    print(f"{record.title()}, what a record!")
    print(f"{record.title()}, what a record again!") # the loop happens on whatever is indented

# if you indent a line where it is not supposed, the python interpreter will throw you a warn

# ofc, we can also do numerical ranges

for value in range(1, 5): # this works without the range() method, but the results are different
    print(value)

# important, this counts 1 to 4 actually. because of the very common off-by-one behavior that happens in computers

# you can also pass the range function with only one number range(6) counts from 0 to 5

# you can also just range() to create lists 

even_numbers = list(range(2, 11, 2)) # the third arugment is the 'step'

squares = [] # empty list

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# goes to 1^2 to 10^2 and puts it on lists. the value and square variables are created there, 
# and SOMEHOW the append function knows that it needs to move the next list slot
# i can only guess that append gets by context that it is appended to a whole list
# well, append probably doesnt work with a single element anyways
# so, it also knows that it is inside a loop. so that's why the interface for incrementing the list 
# doesnt need to exist here

# python also has a few built in numeric functions that shows statistics with lists
# the min, max, sum and others

# python also has LIST COMPREHENSIONS with allows you to do stuff in only a line of code
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# you can also slice a list
print(cubes[1:3])
print(cubes[:3])
print(cubes[5:])
print(cubes[-3:])

# just as we can also do 

for value in cubes:
    print(f"this is a cube {value}")

# we can also do

for value in cubes[2:7]:
    print(f"this is a cube {value}")

# if you want to copy a list, just do this!
new_cubes = cubes # a old school (?) way of doing this is by using new_cubes = cubes[:], which is probably good for code clarity

print(new_cubes)

# and ofc, these are two different and independent lists

# TUPLES

# lists works well for storing collections of items that can change throughout the program, but if you want a const list, use TUPLES

# you define tuples the same you do with lists, but using () instead of [] 

my_t = (1, 3, 4, 56)

# you can't modify the value of the elements in a tulpe

# my_t[2] = 300

# but you can do this 

my_t = (3, 4, 7, 299)

# i guess a truly const tulpe looks like this

MY_T_C = (3123123, 312312)

# just as that goofy philosofy stuff, python has a code style guide. well, at least we have consistance
# look for PEP (python enhancement proporsal)

# ---- IF STATEMENTS ---- 

# well, ifs....

for record in ye:
    if record == 'pablo':
        print(record.upper())
    else:
        print(record.title())

# at the heart of every if statement, there's a expression that can be evaluated as true or false

# we do also have the inequality operator !=

# we do also have the 'and' and 'or' operators

# we do also have boolean expressions such as True or False

universe = True
things = False


if universe:
    print(42)
print("And: ")
if universe and things:
    print(42)

print("Or: ")
if universe or things:
    print(42)

# we also have >= > < <=
# and else and elif, and as you can guess, we can use a lot of elifs
age = 30

if age >= 30:
    print('You still will be fine, chill.')
elif age < 30 and age >= 20:
    print("Enjoy!")
else:
    print("You still a child!")

if 'pablo' in ye: # yeah, we can do this...
    print("30 hours...")

# we can check if a list is empty

available_pizza = ['cheese', 'bacon', 'rice', 'beans', 'bacon', 'fish', 'beer']
requested_pizza = ['rice', 'beer', 'cuscuz', 'bacon']

if requested_pizza: #checks if it is empty
    for requested in requested_pizza:
        if requested in available_pizza:
            print(f"Adding {requested}.")
        else:
            print(f"Sorry, but we don't have {requested}.")
    print("\nYour pizza is done!")
else:
    print("A empty pizza?")

# ---- CHAPTER 6 = DICTIONARIES ----

# this allows you to connect releated pieces of information

enemy = { 'color' : 'green', 'health' : 5, 30 : 'oba-oba'} 

# so... lists [], tulpes (), dictionaries {:}, sets{} (without keys)

print(enemy['health'])
print(enemy['color'])
print(enemy[30])
# print(enemy['green']) # nor this
# print(enemy[5]) # this doesnt work, but


# dictionaries are a key-value list, where the first value is the key we use to reference it, and the second value is the information itself
# both key and values can be a string or a number
# they can also be a list, a tulpa or even other dictionary as a value

# we can also add new values to a dictionary like this

enemy['class'] = 'bard'
print(enemy['class'])

# this just print the entire dictionary
print(enemy)

# this declares a empty dictionary
new_enemy = {}

# interacting with dicts

alien_0 = {'color' : 'green', 'class' : 'sorcerer', 'speed' : 'medium', 'x_pos' : 3, 'y_pos' : 2}

print(f"This alien has a speed of {alien_0['speed']} now.")
print(f"This means he is at x_pos: {alien_0['x_pos']}.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_pos'] += x_increment

print(f"But now he is at x_pos: {alien_0['x_pos']}.")

# we can delete a key-pair from a dict

print(alien_0)

del alien_0['class']

print(alien_0)

# we can also break a dict in multiple files

favorite_records = {
        'jen' : 'white_album',
        'joão' : 'clube_da_esquina',
        'joseph' : '77_live',
        }

# of course, python being picky about identation, we cannot place the open bracket on the line below the indentifier

# anyways, python has a bunch of things to diagnose errors that we will learn after, but we do have the get() method for dicts

class_value = alien_0.get('class', 'alien_0 does not have a class anymore. :(')
print(class_value)

# as you can see, the first argument for get() is a key, and the second one is error string

# we can loop through dicts, as long you dont forget the .items() method

for key, value in alien_0.items(): # we can choose any names for key, value
    print(f"Key = {key}")
    print(f"Value = {value}")

for key in alien_0.keys(): # we also can just use the keys() or values() methods
    print(f"Key = {key}")

for key in alien_0: # these last two loops does the same thing
    print(f"Key = {key}")

for key in sorted(alien_0.keys()): # we can also use sorted() this way
    print(key.title())


favorite_records = {
        'jen' : 'white_album',
        'joão' : 'clube_da_esquina',
        'joão' : 'clube_da_esquina',
        'joseph' : '77_live',
        }

for key, value in favorite_records.items():
    print(f"Key: {key}, Value: {value}")

print("with set()")

for key, value in set(favorite_records.items()):
    print(f"Key: {key}, Value: {value}")

# we can nest dicts and lists

# this is like a array of structs

aliens = []

for n in range(30):
    alien_model = {'color' : 'red', 'speed' : 'medium', 'class' : 'figher'}
    aliens.append(alien_model)

print(aliens)

# we can also do 'structs of arrays':

print("\n\n\n")

pizza = {
        'crust' : 'thick',
        'toppings' : ['mocoto', 'aipim'],
        }

print(pizza)

# you can nest a dict inside another dict, but you code might get complicated real soon(tm)

# CHAPTER 7 = USER INPUTS AND WHILE LOOPS

#this_is_a_input = input("Please input something: ")
#print(this_is_a_input)
#
#input_text = "Please input something again: "
#new_input = input(input_text) 
#
#print(f"Your input was: {new_input}")

# the input function treats every input as a string, to get a numeral input, use the int() function

#age = input("Age: ")
#print(f"New age: {int(age) + 13}")

# ofc you can use the while True: break idiom. continue is also available

# the modulo operator - % - is also available on python

# the while loop:

i = 0;

while i <= 5:
    print(i)
    i += 1

#message = "Write a input, while the input != 'quit', it will spit out what you entered. "
#print(message)
#
#user_input = ""
#
#while user_input != 'quit':
#    user_input = input('Enter something: ')
#    print(f"You entered: {user_input}")

# ofc, we can use the True and False flags with while looops.
# continue is available as well
# and you can use while loops with lists and dictionaries too

#responses = {}
#polling_active = True
#
#while polling_active:
#    name = input("\nWhat is our name? ")
#    response = input("What you like? ")
#    responses[name] = response
#    repeat = input("Is there other person? (yes/no)")
#    if repeat == 'no':
#        polling_active = False
#
#print(" --- POLL RESPONSES --- ")
#for name, response in responses.items():
#    print(f"The person {name.title()} likes {response.title()}.")

# CHAPTER 8: functions

def people_interests(): # defines the function
    responses = {}
    polling_active = True
    while polling_active:
        name = input("\nWhat is our name? ")
        response = input("What you like? ")
        responses[name] = response
        repeat = input("Is there other person? (yes/no) ")
        if repeat == 'no':
            polling_active = False
    print(" --- POLL RESPONSES --- ")
    for name, response in responses.items():
        print(f"The person {name.title()} likes {response.title()}.")

# people_interests() # calls the function

# ofc, you can have arguments for a function

# the common way:

def animal_and_owner(animal='octopus', owner='beatle', age=None): 
    # note that we defined default values, but they are optional, the age argument is made
    # optional with the none
    if age:
        phrase = f"Your animal is {animal.title()} and your name is {owner.title()}, and you are {age} years old."
    else:
        phrase = f"Your animal is {animal.title()} and your name is {owner.title()}."
    return phrase

print(animal_and_owner('dog', 'john'))
print(animal_and_owner('cat', 'paul', '29'))

# but you also can do a name-value pair with keyword arguments
# you specify this on a function call

print(animal_and_owner(animal='parrot', owner='george'))
print(animal_and_owner(owner='ringo', age='30')) # and if the function was defined with default values, we can ommit the arguments in a funciton call

# ofc, you can pass and rerturn lists and dictionaries
# we can also modify them inside a function

# you can prevent a function to modify a list by appending [:] in the end
# function_name(list_name[:])
# you can also have a arbitraty number of arguments using the * operator, also called *args

def albums(*record):
    print(record)

albums('dsotm', 'abbey_road', 'mbdtf')

# there's also **, also called **kargs but we need to learn they later
# we can also store your functions in modules (that in fact are just other files), that you include using import
# you can just do module_name.function_name(), were module_name is just the file_name.py 
# you can also do
# from module_name import function_name
# from module_name import *
# import module_name 
# import module_name as mn
# from module_name import function_name as alias
# and then you call alias()

# CHAPTER 9: CLASSES

# the book tries to evangelise OOP here, 
# so, in OOP you create classes "that represents real-world _things_" and objects based on these classes 
# when you create a class you define the general behavior that a whole category of objects will have

# when you create a object over a class, this is called _instantiation_
# and you work with instances of a class

class dog: # THE FUNCTION THAT IS PART OF A CLASS IS CALLED A METHOD
    # the __init()__ method is a special one that runs automatically everytime we __CREATE__ a object (or a new instance) based on a class
    # the self parameter is also special and required, it needs to be the first one
    # every variable prefixed with self will be accessible for every method in the class
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        print("This is being exec now.")
    def sit(self):
        print(f"{self.name} has {self.age} and now is sitting.")
    def roll_over(self):
        print(f"{self.name} has {self.age} and now is rolling over.")
my_dog = dog("João", 10)

my_dog.sit()
my_dog.roll_over()

# you can also do:

print(f"my_dog name is {my_dog.name} and his age is {my_dog.age}.")

my_other_dog = dog("Pedro", 15)

# and that are the basics of it. but there's more.

# INHERITANCE

# we always can start a new class from scratch, but we are also able to inherit a child class that provides specialized functionality

class electric_dog(dog):
    def __init__(self, name, age, battery):
        self.battery = battery
        super().__init__(name, age) 
    def battery_information(self):
        print(f"{self.name} has {self.age} and his battery points is {self.battery}.")
    def roll_over(self):
        print(f"{self.name} has {self.age} and now is rolling over even more!")

my_e_dog = electric_dog("Joaquim", 20, 65)

my_e_dog.sit()
my_e_dog.roll_over()
my_e_dog.battery_information()

# super() thing on the __init__ method is a special function that allows you to call a method from a parent class. the name super comes from calling a
# convention of calling a parent class a superclass and a child subclass 
# in this case we are calling the __init__ method, but we could call any others my_e_dog = electric_dog("Joaquim", 20, 50)
# we overide a method from a parent class just by redefining it

# you can also import a class from other file using
# from dog import electric_dog 
# where dog is a dog.py file, which are also called a MODULEA
# ofc we can also just do
# from dog import *
# annnnnd offfc you can import a module into a module, but that doesnt metter rn

# THE PYTHON STD LIB

# yes, there's one

# there are funtionality that is available in every python installation
# and you can have more by using pip

from random import randint
from random import choice

print(randint(1, 6)) # this gives you a random number everytime you run it
print(choice(ye))    # this gives you a random record everytime you run it

# CHAPTER 10: FILES AND EXCEPTIONS

from pathlib import Path

print(Path('C:/Users/LEO/Desktop/pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt').read_text())
print(Path('C:/Users/LEO/Desktop/pcc_3e-main/chapter_10/reading_from_a_file/pi_digits.txt').read_text().rstrip()) # this is called method chaining
# print(Path('C:/Users/LEO/Desktop/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt').read_text())

# remember that on windows we need change to foward slash

############ - HOW TO READ A FILE - ################

# #01: stores the path of the file on a variable
pi_mi = Path('C:/Users/LEO/Desktop/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt') 
print(pi_mi)

# #02: reads the text
content = pi_mi.read_text() 
print(content)

# #03: the splitlines() method split lines into a list
lines = content.splitlines()  
print(lines)

# 04: the lstrip() removes left spaces from a string (that's why we need to make a loop)
# this loops also get back to join everything back to a string
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)

# 05: you can search for a smaller string in a bigger one by just doing a simple loop like this

#bday = input("Enter your b-day on the format ddmmyyyy: ")
#if bday in pi_string:
#    print("Your birthday is on pi!")
#else:
#    print("Your birthday is not on pi!")

############ - HOW TO READ A FILE - ################

# how to access lines
contents = Path('C:/home/misc/file.txt').read_text() # this is called method chaining
lines = contents.splitlines()

print(lines)

print(sorted(lines)) # the syntax for sorted()

lines.sort() # the syntax for sort()
print(lines)

# again: the difference between sort and sorted:
# sort is a method of the list class and can only be used with them, it modifies the actual list and returns None
# sorted() is a general method that accepts any iterable object, and has the syntax sorted(_thing_), that returns the sorted list

############ - HOW TO WRITE A FILE - ################

# 01: the path of the file you want to write

write_path = Path('c:/home/misc/write_python.txt')

write_contents = "This is a file.\n"
write_contents += "That is being writting.\n"
write_contents += "Right now.\n"
write_contents += "Over me.\n"
write_contents += "Shooot!.\n"

write_path.write_text(write_contents)

############ - HOW TO WRITE A FILE - ################

# EXCEPTIONS

# python has special objects called exceptions that manages errors that arise during a program execution

# print(1235/0)

print("Does the program continue execution anyways?") # no!!!!!

# when you do a division by zero, a excpetion object, ZeroDivisionError, runs. 

# we can use a try-except block to handle errors

try:
    my_text = Path("C:/home/misc/non_file.txt").read_text()
except:
    print("ERROR: This file doesnt exist.")

# using these blocks allows python to continue running the code

# we can use try-except blocks between a if-else block

# so, the basic behavior is: without a try-except block, python stops running the program, with it the program continuous

try:
    my_text = Path("C:/home/misc/write_python.txt")
except:
    print("ERROR: This file doesnt exist.")
else:
    file_read = my_text.read_text()
    words = file_read.split()
    print(f"This file {my_text} has about {len(words)} words.")

# storing data using json

import json

try:
    my_file = Path("C:/home/misc/numbers.json")
    contents = json.dumps(enemy)
    my_file.write_text(contents)
except:
    print("ERROR: Can't write to this file.")
else:
    print("SUCCESS: Exported the enemy dictionary to json.")

# this is a useful way to store data generated by the users
# the json blends well with pythons' data structures
