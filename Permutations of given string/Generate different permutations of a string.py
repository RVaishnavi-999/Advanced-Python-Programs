# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:34:01 2021

@author: Vaishnavi R
"""
"""3. Program to generate different permutations of a given string using functions."""
def permute(s,e):    #user defined function permute
    size=len(e)
    if size == 0:
        print(s)
    else:
        for i in range(size):
            ns=s + [e[i]]
            ne=e[ :i] + e[i + 1:]  #slicing 
            permute(ns,ne)    
s=input("enter a string  : ")
a=[]
for i in range(len(s)):
    a.append(s[i])
permute([   ],a)
