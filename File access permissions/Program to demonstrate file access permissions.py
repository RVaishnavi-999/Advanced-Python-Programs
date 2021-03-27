# -*- coding: utf-8 -*-
"""
@author: Vaishnavi R
"""
"""5. Program to demonstrate File access permissions such as create, write, read and delete options."""

import os
Ans = "y"
while Ans =="y":
    print ("1.Create a file")
    print("2.Read the file")
    print("3.Delete the file")
    print("4.Exit")
    y=eval(input("\nSelect your option"))
    if y==1:
        filename=input("Enter file name to create and write content : ")
        c=open(filename,"w")
        print("\nThe file,",filename,"Created successfully!")
        print("Enter the content of the file")
        sent1=input()
        c.write(sent1)
        c.close()
        print("\nContent successfully placed inside the file")
    elif y==2:
        filename=input("Enter file name (with extension)to read")
        c=open(filename,"r")
        print("\n the file,",filename,"contains")
        print(c.read())
        c.close()
    elif y ==3:
        filename=input("enter file name to delete")   
        #existed file will be deleted, if a file is not created then FileNotFoundError will appear
        print("Removing the file")
        os.remove(filename)
        print("\n the file,",filename,"Successfully deleted!!")
    elif y == 4:
        print("Thank you")
        break

    Ans=input("\nDo you want to continue:(Y/N)")