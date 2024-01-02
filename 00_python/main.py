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


