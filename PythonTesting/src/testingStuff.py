# Here im printing stuff

# print("Bob is awesome")


#variable stores information
#integer (int) variable holds a whole number

# age=100
# print(age)
# print(type(age))

# something is the variable, 25 is the information

#floating point variable holds a decimal

# decimalStuff = 12.2
# print(age)
# print(decimalStuff)

#String variable holds a word

# words = "apples"
# print(words)
# #
# print(type(words))
# print(words*age)

# # Break sequences in strings
# moreWords = "This is a test to see what happens"
# print(moreWords)
# moreWords = "This is a \"test to see what\" happens"
# print(moreWords)
# moreWords = "This is a \'test to see what\' happens\'"
# print(moreWords)
# moreWords = "This is a \\test to see what \\happens"
# print(moreWords)
# moreWords = "This is a \ntest to see \nwhat happens"
# print(moreWords)
#
# #formated strings
# first = "Tom"
# last = "Smith"
# full = first+" "+last
# print(full)
# #
# full = f"{first}       {last}"
# print(full)
#
# full = f"{4} \n {5+6+56} {first}"
# print(full)


#Boolean Variables hold conditions True or False (Must be capitalized)

# condition = True
# otherCondition = False
#
# if (otherCondition):
#     print("This is true")
# else:
#     print("Not true")

#Programs get executed from top to bottom. If you use the same variable it gets overridden

age = 56
print(age)
decimalStuff = 12.3
# You can do math

# age2 = age+decimalStuff
# age3 = age/decimalStuff
# age4 = age-decimalStuff
# age5 = age*decimalStuff
# print(age2)
# print(age3)
# print(age4)
# print(age5)
#
# Extra math
# // gives you the whole number. Gets rid of the numbers left of the decimal
age6 = age//decimalStuff
print(age6)

# % is known as the mod. It returns the remainder of the division
age7 = age%decimalStuff
print(age7)

# ** two multiplications is the exponent. It is age to the power of decimalStuff
age8 = 56**12.3
print(age8)

# Augmented operators
# newAge = 20
#
# newAge = newAge + 5
# print(newAge)
#
# newAge +=5
# print(newAge)
#
# newAge = newAge - 10
# print(newAge)
#
# newAge -=10
# print(newAge)
#
# newAge *=2
# print(newAge)
#
# newAge /=3
# print(newAge)

# Order of operations = Same as in math (mod counts as a type of divison)
# x = 10+3*5
# print(x)
#
# x = (10+3)*5
# print(x)


# Careful with Strings and numbers

# stris = "5"
# numb = 10
#
# addStuff = str+numb
# print(addStuff)


# Getting input (by default it is String)

# username = input("What do you want your username to be?: ")
# print("This is your username: "+username)

# if you want an integer so you can do math you have to recast it
# to print it you have to recast it as a string

# intIWant = int(input("This is the int I want: "))
# print("This is the int you wanted "+str(intIWant))

# int doesn't have a decimal place. They are a whole numbers. 
# If you want to be able to have a decimal place you have to use float

# floatIWant = float(input("This is the float I want: "))
# print("This is the float you wanted "+str(floatIWant))

# You can also recast into a boolean
# But be careful. When using it directly on the input it just checks if they put something in.

# boolIwant = bool(input("Is the statement True or False?: "))
# print(boolIwant)
#
# if (boolIwant is True):
#     print("The statement is True")
# else:
#     print("The statement is False")

# Some built in functions

# name = "matt smith"
#
# print(name.capitalize())
# print(name.upper())
# print(name.isprintable())
# print(name.__len__())
#
# # Think of a String as a list of characters. The list starts with 0
#
# print(name.find("s"))
#
# print(name.replace("smith", "johnson"))
#
# # Careful when just usign print because you haven't saved it
# print(name)
#
# #Using the in operator
#
# print("matt" in name)
# print("bob" in name)
#
# name = name.replace("smith", "johnson")
#
# if("smith" in name):
#     print("Name is common")
# else:
#     print("Name is not common")


# Comparison operators

# isit = 3 > 2
# print(isit)
#
# isit = 3 < 2
# print(isit)
#
# isit = 3 >= 2
# print(isit)
#
# isit = 3 <= 2
# print(isit)
#
# isit = 3 == 2
# print(isit)
#
# # ! means NOT
# isit = 3 != 2
# print(isit)
#
# # not means NOT when you want the opposite of something
# tom = not isit
# print(tom)
# print(not tom)

# Logical operators ->  and  or

# age = 45
# print(age>35)
#
#
# print(age>35 and age<40)
#
# print(age>60 or age<50)


# if elif else
#
# tom = 45
#
# if (tom<35):
#     print("He is young")
# elif (tom<12):
#     print("He is very young")
# else:
#     print("He is old")
# print("this is the end")

#in one line if not complex
# tom = 45
# if (tom<35):
#     message = "He is young"
# else:
#     message = "He is old"
# print(message)
#
# message = "He is young" if tom<35 else "He is old"
# print(message)



# while loops

# price = 20
# while (price>10):
#     print("Too much")
#     price -= 1 # must make sure to have something in the loop to terminate the sequence by making the condition false. 
#     # If not it will go on forever.
# print("Just right")


# Lists

# names = ["Bob", "Tom", "John", "Matt", "James"]
# print(names)
# print(names[3]) # remember index starts at 0
# names[4] = "Ash" # replace 
# print(names)
# print(names[1:4]) # just want a few

# something = "Tom Smith"
# print(something[1:4])
# print(something.replace("o", "i"))
#
#
# numbers = [1,2,5,8,34,25,16,1,2,3]
# print(numbers)
# #print(numbers[8]) # don't go over
# print(numbers[-1]) # the last one
# print(numbers[-2]) # second to last one
#
# # List operations
# numbers.append(3)
# print(numbers)
# numbers.insert(4, 90)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# print(len(numbers)) # how many elements
# print(numbers.count(2)) # how many 2 are in the list
# print(numbers.index(34)) # where is 34?
# numbers.clear()
# print(numbers)

#check for info in list
# numbers = [1,2,5,8,34,25,16]
# names = ["Bob", "Tom", "John", "Matt", "James"]
#
# print("Tom" in numbers)
# print(2 in numbers)
# print(2 in names)
# print("Tom" in names)
# print("Tom " in names) # Careful

# for loops

# numbers = [1,2,5,8,34,25,16]
# names = ["Bob", "Tom", "John", "Matt", "James"]
#
# for things in numbers:
#     print(things)
#
# for stuff in names:
#     print(stuff)
#
# # same thing with while loops
# index = 0
# while (index<len(numbers)):
#     print(numbers[index])
#     index+=1
#
# # while loops give you more flexibility
# index = len(numbers)-1
# while(index>=0):
#     print(numbers[index])
#     index-=2
    

# Using range funciton
# numbers2 = range(0,10)
# print(numbers2)
#
# for stuff in numbers2:
#     print(stuff)
    
# numbers3 = range(5,15)
# for things in numbers3:
#     print(things)

# break - get out of loop

# numbers3 = range(0,20)
# for stuff in numbers3:
#     if (stuff == 4):
#         print("Found it")
#         break
#     print("Not yet")
# print("done")

# functions
# def goingUp (number, upBy):
#     finalNum = number+upBy
#     return finalNum
#
# info = goingUp(10,5)
# print(info)
#
# #Using it from somewhere else
# import moreTesting
#
# info2 = moreTesting.moreStuff(10, 15)
# print(info2)
#
# info3 = moreTesting.moreStuff(10.5)
# print(info3)
#
# apples = [10, 4, 5, 7]
# print(moreTesting.moreStuff2(apples))




    
    

