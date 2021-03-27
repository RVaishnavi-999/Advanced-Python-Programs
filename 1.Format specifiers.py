# -*- coding: utf-8 -*-
#%%
"""1. Program to demonstrate format specifiers of python 
by calculating interest and principle amount for ‘n’ 
number of years."""

p=eval(input("enter the principal amount"))
t=eval(input("enter the time given"))
r=eval(input("enter the rate of interest"))
#format method  synatx()
print(format("term","10s")+format("per","12s")+format("PA","12s")+format("IR","12s")+format("tot","10s"))
for i in range(1,t + 1):
    ip=p * r / 100
    tot=p + ip
    print(format(i,"3d"),format(r,"13.2f"),format(p,"10.2f"),format(ip,"10.2f"),format(tot,"10.2f"))
    p=tot