# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:32:14 2021

@author: Vaishnavi R
"""
"""4. Menu driven program to demonstrate the usage of os, socket and glob library functions."""
import os
import socket
import glob
Ans="y"

while Ans == "y":
    print("1. open Notepad")
    print("2. Get IP Address")
    print("3. List the files in the Directory")  #only lists word doc,pdf, links not other files
    print("4. Exit")

    y=eval(input("\nSelect your option : "))
    if y == 1:
        os.system('start notepad.exe')
    elif y == 2:
        print("\nYour IP Address is : ",end="");
        print(socket.gethostbyname(socket.gethostname()));
    elif y == 3:
        x= input("\nEnter the directory path : ")
        os.chdir(x)
        print("List of files in the directory are : ")
        for file in glob.glob("*.*"):
            print(file)
    elif y == 4:
        print("\nThank you")
        break
    
    print()
    Ans=input("Do you want to continue:(Y/N)")