"""
Created on Mon Sep 13 13:47:15 2021

@author: Sameer Prasanna
"""
''' Income Tax Calculation Management System (ITCMS)
Version 0.1 '''

#Alpha Build

''' this build is with no imported tables
purely build on python functions'''

import pandas as pd
#import numpy as np

print("INCOME TAX CALCULATION MANAGEMENT SYSTEM")
print("Please Enter the following data - ")

PAN=input("Enter Permanent Account Number(PAN): ")
aadhar=input("Enter your Aadhar card No: ")
name=input("Enter Name: ")
mobileno=input("Enter Mobile No: ")
income=int(input("Enter Total Income during the year: "))
rate=0.0
tax=0

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
print("INCOME TAX REPORT")
print()
print("Name : ",name)
print("PAN number : ",PAN)
print("Aadhar Number : ",aadhar)
print("Mobile number : ",mobileno)
print("Total Income during the year : ",income)
print("Rate of Taxation : \t",rate*100,"%")
print("Amount of income tax to be paid : ",tax)
print("-------------------------------------------------------------------------------------------------------------------")
