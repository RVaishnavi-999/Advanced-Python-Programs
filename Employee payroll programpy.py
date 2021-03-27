# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""8. Program to calculate the employee weekly payroll using method 
overloading concept."""
class emp:
    def weekly_pay(self,whrs=None,pay=None,ohrs=None):
        if whrs!=None and pay!=None and ohrs!=None:
            total=whrs*pay+ohrs*pay
            print("total pay of employee is ",total)
        elif whrs!=None and pay!=None:
            total=whrs*pay
            print("total pay of employee is",total)
e=emp()
whrs=eval(input("enter hours worked by employee: "))
ohrs=eval(input("enter the hours worked over time: "))
pay=eval(input("enter the pay per hour: "))
if ohrs>0:
    e.weekly_pay(whrs,pay,ohrs)
else:
    e.weekly_pay(whrs,pay)