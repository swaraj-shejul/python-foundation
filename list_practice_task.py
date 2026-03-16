# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:07:19 2026

@author: swaraj
"""

#===============================================================================================================
# Given the list numbers = [10, 20, 30, 40, 50], print the second and fourth elements of the list?

l = [10, 20, 30, 40, 50]

print(l[2::2])

#===============================================================================================================
# Given the list of numbers = [1,2,3,4,10,9,8,4], print the last three numbers using slicing?

l = [1,2,3,4,10,9,8,4]

print(l[-3::1])

#===============================================================================================================
# Create a list of numbers and print both the maximum and minimum values in the list using the max() and min() functions?


l = [1,2,3,4,10,9,8,4]
print(max(l))
print(min(l))


#===============================================================================================================
# Create a list of letters, sort them and print the list in reverse order?

s = "swarajpravinshejul"
s = " ".join(s)
l = s.split()
l.sort(reverse=True)
print(l)


#===============================================================================================================
#  Create a list of strings and count how many times a specific string appears in the list using the tount() method?


l = ["swaraj"] * 7

print(l.count("swaraj"))


#===============================================================================================================
# create a list of colours. change the first colour to last colour of the list and vice-versa,print the updated list?

l = ["yellow", "orange", 'green', 'red', 'black', 'pink', 'blue', 'purple', 'white']

l[0], l[-1] = l[-1], l[0]
print(l)


#===============================================================================================================
# write a code for getting "hello" as output from the given list?

l = [25,30,[26,27,28,"hello"],[32,38]]
print(l[2][3])



#===============================================================================================================
# For the above given list replace 27 with 43

l = [25,30,[26,27,28,"hello"],[32,38]]
l[2][1]=43
print(l)

#===============================================================================================================
# Insert a value "True" at last second position?

l = [25,30,[26,27,28,"hello"],[32,38]]

l.insert(3, True)
print(l)

#===============================================================================================================
#  create an empty list and ask user to enter their favourite fruits to the empty list using append methods?

l = []
i = input("enter fruit names space seperated : ")
l.append(i)
print(l)



#===============================================================================================================
#  To the above created list. Add three more fruits at once?
l = ['mango', 'banana']
l.extend(["apple", "greps", "watermalon"])
print(l)


#===============================================================================================================
# Sort the above created list using list method?
l = ['mango', 'banana', 'apple', 'greps', 'watermalon']
l.sort()
print(l)

#===============================================================================================================
# Given a List [4, 5, 1, 2, 9,7, 10, 8].Find the sum and average of the list?

l = [4, 5, 1, 2, 9,7, 10, 8]

print(sum(l))
print(sum(l)/len(l))

#===============================================================================================================
# Remove the last fruit from the list using pop().

fruits = ['apple', 'banana', 'orange', 'mango']
fruits.pop(-1)
print(fruits)

#===============================================================================================================
# Write a Python program to clone or copy a list?

fruits = ['apple', 'banana', 'orange', 'mango']

# 1)  reference copy
a = fruits
# 2) shallow copy
b = fruits.copy()


#===============================================================================================================
# Write a Python program to append a list to the second list?

l = [4, 5, 1, 2, 9,7, 10, 8]
l2 = ['apple', 'banana', 'orange', 'mango']

l.append(l2)

print(l)



#===============================================================================================================
# Write a program that counts how many times a specific element appears in a list?

l = ['w', 'v', 'u', 's', 's', 'r', 'r', 'p', 'n', 'l', 'j', 'j', 'i', 'h', 'e', 'a', 'a', 'a']

print(l.count('a'))

#===============================================================================================================
# Write a Python program to find the second smallest number in a list?

l = [4, 5, 1, 2, 9,7, 10, 8]

l.sort()
print(l[1])


#===============================================================================================================
# Write a Python program to get unique values from a list?

l = ['w', 'v', 'u', 's', 's', 'r', 'r', 'p', 'n', 'l', 'j', 'j', 'i', 'h', 'e', 'a', 'a', 'a']

for i in l:
    if l.count(i) == 1:
        print (i)

#===============================================================================================================
# Write a program that reverses the elements of a list?

l = ['apple', 'banana', 'orange', 'mango']
l.reverse()
print(l)

#===============================================================================================================
# Count how many times a specific item appears in a list?

l = ['w', 'v', 'u', 's', 's', 'r', 'r', 'p', 'n', 'l', 'j', 'j', 'i', 'h', 'e', 'a', 'a', 'a']
l2 = []
for i in l:
    if i in l2:
        l2.count(i)
    else:
        l2.append(i)

for i in l2:
    print(f"{i} = {l.count(i)}")
    
    

#===============================================================================================================
#   Reverse a list using slicing?
l = [4, 5, 1, 2, 9,7, 10, 8]
print(l[::-1])


#===============================================================================================================
# Replace the last item in a list with "Pineapple"?


l = ['apple', 'banana', 'orange', 'mango']
l[-1] = "Pineapple"
print(l)


#===============================================================================================================
# write a python program to concatenate items of the list to a single item?


l = ['apple', 'banana', 'orange', 'mango']

l = list(["".join(l)])
print(l)


#===============================================================================================================
# write a python code to copy list of fruits using slicing method?


l = ['apple', 'banana', 'orange', 'mango']

l2 = l[::]

print(l2)

#===============================================================================================================
# How do you access the second element of the second list in a nested list.

nested = [[1, 2], [3, 4], [5, 6]]

print(nested[1][1])