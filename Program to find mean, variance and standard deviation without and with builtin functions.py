# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""12. Program to find mean, variance and standard deviation without and with builtin functions"""
import math
import statistics
n=int(input("Enter the number of observations:"))
obs=[]
print("Enter ",n," observations")
for i in range(0, n):
    obs.append(int(input()))
mean=sum(obs)/n
deviations = [(x - mean) ** 2 for x in obs]
variance = sum(deviations) / n
stddev=math.sqrt(variance)
print("Mean without using builtin function :",mean)
print("Variance without using builtin function:",variance)
print("Standard Deviation without using builtin function:",stddev)
print("Mean by using builtin function:",statistics.mean(obs))
print("Variance by using builtin function:",statistics.pvariance(obs))
print("Standard Deviation by using builtin function:",statistics.pstdev(obs))
