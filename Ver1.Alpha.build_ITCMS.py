"""
Created on Mon Sep 13 13:47:15 2021

@author: Sameer Prasanna
"""
"""
Income Tax Calculation Management System (ITCMS)
Version 0.1
"""
#Alpha Build
"""
This build is with no imported tables
purely build on python functions
"""
import pandas as pd
#import numpy as np
print("------------------------------------------------------------------------------------------------------------------")
print()
print("INCOME TAX CALCULATION MANAGEMENT SYSTEM")
print()
print("Please Enter the following data - ")
print()
PAN=input("Enter Permanent Account Number(PAN): ")
print()
aadhar=input("Enter your Aadhar card No: ")
print()
name=input("Enter Name: ")
print()
mobileno=input("Enter Mobile No: ")
print()
income=int(input("Enter Total Income during the year: "))
print()
rate=0.0
tax=0
print("------------------------------------------------------------------------------------------------------------------")
print()

#Tax slabs via conditional statements
if income<=250000:
    rate=0
    print("No Income tax has to be paid by you.")

if income>=250001 and income<=500000:
    rate=0.05

if income>=500001 and income<=750000:
    rate=0.1

if income>=750001 and income<=1000000:
    rate=0.15

if income>=1000001 and income<=1250000:
    rate=0.2

if income>=1250001 and income<=1500000:
    rate=0.25

if income>1500000:
    rate=0.3

tax=rate*income

# - Commands to make a DataFrame from input data here

taxpayer=pd.DataFrame(columns=("PAN number"," Aadhar Number"\
,"Name","Mobile Number","Total Income","Rate of tax(in%)",\
"Income Tax"),index=None)

taxpayer.at[0]=[PAN,aadhar,name,mobileno,income,rate*100,tax]

# - Commands for displaying report

print("------------------------------------------------------------------------------------------------------------------")
print()
print("INCOME TAX REPORT")
print()
print("Name : \t\t\t\t\t\t\t ",name)
print()
print("PAN number : \t\t\t\t\t ",PAN)
print()
print("Aadhar Number : \t\t\t\t ",aadhar)
print()
print("Mobile number : \t\t\t\t ",mobileno)
print()
print("Total Income during the year :   ",income)
print()
print("Rate of Taxation : \t\t\t\t ",rate*100,"%")
print()
print("Amount of Income tax to be paid :",tax)
print()
print("-------------------------------------------------------------------------------------------------------------------")
