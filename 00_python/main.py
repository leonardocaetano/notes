# so... python has variables... and also f-strings

# in python a variable is a not a box, but a _label_ (a pointer? a reference?)

from re import A


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

# the difference between single and double quotes:

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

# NOTE: the remove() method only remove the first appearence of a element, you need to use a loop to make sure all elements that are the same is remove

# for last, you can manually change a specific element of the list

steely_dan[0] = 'the_nightfly'

# you can also use the insert and delete with lists, you can also sort them!!!

steely_dan.sort()
print(steely_dan)
steely_dan.sort(reverse=True)
print(steely_dan)

# vim note: when in visual mode, the cursor position is also selected
# the pasting happens after the cursor, and below!!!

# back to lists: yeah, there's a lot of methods you can apply to it... reverse, sort, len, sorted...
# the difference between sort and sorted is that sorted criates a new list, while sort affects the original

# ---- WORKING WITH LISTS ----

ye = ['cd', 'lr', 'grad', '808s', 'mbdtf', 'yee', 'pablo', 'jik', 'd', 'd2']

# we can now loop!!!!

for record in ye:  # the record variable gets created here
    print(record)

for record in ye:  # well, i guess that it is also impotant to note that this range is [inclusive]
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


