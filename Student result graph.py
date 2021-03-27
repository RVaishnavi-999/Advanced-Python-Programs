# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""7. Program to calculate ‘n’ number of student result and generate a result analysis 
bar graph between each student."""

import matplotlib.pyplot as plt
ans='y'
av=[]
nm=[]
rt=[]
while ans=='y':
    nam=input("enter the student name:")
    nm.append(nam)
    nam=[]
    i=0
    avg=0
    tot=0
    while i != 5:
        sub=eval(input("enter each subject marks:"))
        nam.append(sub) 
        tot=tot+nam[i]
        avg=tot/5
        i=i+1
    if min(nam)<35:
        res="fail"
    else:
        res="pass"
    av.append(avg)
    rt.append(res)
    ans=input("do you want to continue data:(y/n)")
d1=dict(zip(nm,av))
print("student list along with average marks:",d1)
d2=dict(zip(nm,rt))
print("student list along with average marks:",d2)
plt.bar(nm,av,align="center",alpha=0.5,label="sname",color='r')
plt.legend()
plt.ylabel('performance')
plt.xlabel('subjects')
plt.title('programming language usage')
plt.show()
