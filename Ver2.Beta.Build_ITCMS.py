#<Code info>
"""
Created on Wed Sep 22 12:01:39 2021

@author: Sameer Prasanna
"""
'''
Income Tax Calculation Management System (ITCMS)
Version 0.2
'''
#Beta Build # Final Build
'''
This build is with 1 imported table
TAXSLAB table to be imported from MySQL
TAXSLAB Table has fixed data of Tax slabs
and all the user data is to be inputted
and exported to MySQL 'Taxpayer' Table
'''
#</Code info>

"""
PRE REQUISITES-

SQL database - ITCMS (CREATE DATABASE ITCMS;)

Table - Taxslab
CREATE TABLE Taxslab
(tsid varchar(2) PRIMARY KEY,rate varchar(4),llimit int,ulimit int, mrate float);

Taxslab data - 
INSERT INTO Taxslab VALUES
("t1","0%",0,250000,0),("t2","5%",250001,500000,0.05),
("t3","10%",500001,750000,0.1),("t4","15%",750001,1000000,0.15),
("t5","20%",1000001,1250000,0.2),("t6","25%",1250001,1500000,0.25),
("t7","30%",1500001,9999999999,0.3);

Table - Taxpayer
CREATE TABLE Taxpayer
(PAN varchar (12),AadharNo varchar(12),Name varchar(25),mobileno varchar(10),income int,rate float,tax int);
"""

#<Import Statements>
import pandas as pd
import mysql.connector as msctr
import pymysql
from sqlalchemy import create_engine
#import numpy as np
#</Import Statements>

#Connecting to Database
con=msctr.connect(host="localhost",user="root",passwd="12345",database="ITCMS")
dfts=pd.read_sql("SELECT * FROM Taxslab;",con)
if con.is_connected():
    print("Successful connection to MySQL Database")

#Inputting Data for Taxpayer
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
 
#Conditional Statements for determining rate and Tax to be paid
if income<=250000:
    rate=dfts.mrate[0]
    print("No Income tax has to be paid by you.")

if income>=250001 and income<=500000:
    rate=dfts.mrate[1]

if income>=500001 and income<=750000:
    rate=dfts.mrate[2]

if income>=750001 and income<=1000000:
    rate=dfts.mrate[3]

if income>=1000001 and income<=1250000:
    rate=dfts.mrate[4]

if income>=1250001 and income<=1500000:
    rate=dfts.mrate[5]

if income>1500000:
    rate=dfts.mrate[6]

tax=rate*income

#Commands to create the Tax payers DataFrame
taxpayer=pd.DataFrame(columns=("PAN number"," Aadhar Number"\
                                   ,"Name","Mobile Number","Total Income","Rate of tax(in%)",\
                                      "Income Tax"))
    
taxpayer.at[0]=[PAN,aadhar,name,mobileno,income,rate,tax] #If using spyder use int(tax)
print()

# - Commands for displaying report
print("------------------------------------------------------------------------------------------------------------------")
print()
print("INCOME TAX REPORT")
print()
print("Name : \t\t\t\t\t",name)
print()
print("PAN number : \t\t\t\t",PAN)
print()
print("Aadhar Number : \t\t\t",aadhar)
print()
print("Mobile number : \t\t\t",mobileno)
print()
print("Total Income during the year :   ",income)
print()
print("Rate of Taxation : \t\t\t",rate*100,"%")
print()
print("Amount of Income tax to be paid :",tax)
print()
print("-------------------------------------------------------------------------------------------------------------------")

#Code to export the Taxpayer DataFrame to MySQL
dbengine=create_engine('mysql+pymysql://root:12345@localhost/ITCMS')
connn=dbengine.connect()
taxpayer.to_sql('taxpayer',connn,index=False,if_exists='append')

#Closing Connections to Database
con.close()
connn.close()
