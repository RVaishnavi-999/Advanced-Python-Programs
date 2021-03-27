# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""6. Program to count the occurrence of a word in a file."""
fname=input("enter file name: ")
word=input("enter word to be searched: ")
k=0
with open(fname,'r')as f:
    for line in f:
        words=line.split()
        for i in words:
            if i==word:
                k=k+1
print(word+" appears in the file : ",k," times")
