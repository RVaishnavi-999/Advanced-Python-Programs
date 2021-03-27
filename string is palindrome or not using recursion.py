# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""10. program to check whether a given string is palindrome or not using recursion"""
def palindrome(s,first,last):
    if last <= first:
        return "Palindrome"
    elif s[first] != s[last]:
        return "Not palindrome"
    else:
        return palindrome(s,first+1,last-1)
s=input("Enter string : ")
res=palindrome(s,0,len(s)-1)
print(s, " is ",res)