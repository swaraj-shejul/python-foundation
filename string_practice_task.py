# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:16:29 2026

@author: swaraj
"""
# ===========================================================================================================
# print string in reverse
#========================
repeat = True

while repeat == True:
    i = input(" enter a string which want in reverse :")
    print ( f" the given string has been reversed = {i[::-1]} ")
    
    i = input(" wan't to repeate it press enter if want to exit enter anything and press enter")
    if i != "":
        repeat = False
    else:
        continue
    

#===========================================================================================================
# check the string is palindrom or not
#=====================================

s = input(" enter a string which want to check for palindrom :")
s1 = s[::-1]
if s == s1:
    print ("True")
else:
    print("False") 
   
#=========================================================================================================
# replace " " space with "_"
#==========================

i = input("give the string with containing spaces :")
r = i.replace(" ", "_")
print (r)


#========================================================================================================
# Count how many times given character appears in a string .
#=============================================================

s = input("Enter the string : ")
c = input("Enter the charecter to check its number of appearance : ")

print(s.count(c))

#========================================================================================================
# Find the index of the first occurrence of a character.

s = input("Enter the string : ")
c = input("Enter the charecter to find its first occurance index number : ")
print(s.index(c))

#========================================================================================================
# Convert all characters into uppercase.

s = input("Enter the string : ")
print(f"upper case string : {s.upper()}" )


#========================================================================================================
# join two string

s = input("Enter the string : ")
s2 = input("Enter the 2nd string : ")
s3= s+s2
print(f"joined string : {s3}")


#========================================================================================================
#Remove all occurrences of specific character "m" from programming word.

w = "programming"
w = w.replace("m","")
print(w)


#========================================================================================================
# Extract "gram" from the string "programming".

w = "programming"
print(w[3:7])


#========================================================================================================
# Find the number of characters in a string hello world.

s = "hello world"
print(len(s))

#========================================================================================================
# Change "hello world how are you" to "hello-world-how-are-you".

s = "hello world how are you"
s = s.replace(" ", "-")
print(s)

#========================================================================================================
# Remove leading and trailing spaces for the string " messy text ".

s = " messy text "

s = s.strip()
print(s)


#========================================================================================================
# Check if the string "Hi there" starts with "Hi".


s = "Hi there"

s.startswith("Hi")


#========================================================================================================
# Check is the string "I am running" ends with "ing"

s = "I am running"
s.endswith("ing")

#========================================================================================================
# Capitalize only the first letter of the sentence "welcome to the jungle"

s = "welcome to the jungle"
s = s.capitalize()
print(s)

#========================================================================================================
# Join a list of words into a sentence

l = ["I", "love", "coding"]

s = " ".join(l)
print(s)

#========================================================================================================
# Make the string "Python Is Fun" lowercase and replace spaces with underscores.

s = "Python Is Fun"

s = s.replace(" ", "-").lower()
print(s)


#========================================================================================================
# Reverse the words "hello world python" into "python world hello".

s = "hello world python"
s = s.split()
s.reverse()
s = " ".join(s)
print(s)


#========================================================================================================
# Extract only alphabets at even positions.

s = "aXbYcZd"

print(s[::2])



#========================================================================================================
# Task: Swap first and last character of the string.

s = "Tomorrow"
s = " ".join(s)
l = s.split()
l[0], l[-1] = l[-1], l[0]

s = "".join(l)
print(s)


#========================================================================================================
# Add # between each letter of the word.

s = "tomorrow is holiday"

s = "#".join(s)
print(s)

