# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""9. Program to demonstrate file handling exceptions."""
def main():
    cl=[0] *26
    try:
        fn=input("Enter file name: ")
        infile=open(fn,"r")
        for line in infile:
            print(line)
            cls(line,cl)
        infile.close
    except FileNotFoundError:
        print(fn,"is not found")
    else:
        f=0
        for i in range(len(cl)):
            if cl[i]!=0:
                f=1
                print(" char ",chr(ord('a')+ i) + " appears "+str(cl[i])+" times ")
        if f==0:
            print("no character found")
def cls(line,c):
    for ch in line:
        if ch.isalpha():
            p=ord(ch.upper()) - ord('a')
            c[p]+=1
            
main() 