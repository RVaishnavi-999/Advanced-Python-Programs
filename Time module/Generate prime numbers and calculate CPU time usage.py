# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""2. Program to generate prime numbers and calculate CPU time using time module."""

from time import process_time
m=eval(input("Enter max range :"))
c=0
st=process_time()
for i in range(2,m+1):
    f=0
    for j in range(2,i):
        if i%j == 0:
            f=1
            break
    if f==0:
        print(i, end= " ")
        c+=1
        
print()
el = process_time()-st
print("Number of prime numbers : ",c)
print("Time elapsed : " ,el, " seconds")
