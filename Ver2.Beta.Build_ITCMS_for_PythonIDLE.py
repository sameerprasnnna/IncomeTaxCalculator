'''
Documentation
System used : Windows 10 64 bit
Environment used : Python 3.8.5 IDLE
'''
#<Code info>
"""
Created on Wed Sep 22 12:01:39 2021

@author: Sameer Prasanna
"""
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

Modules -

mysql.connector
sqlalchemy
pymysql

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
CREATE TABLE taxpayer
(PAN_number varchar (12),Aadhar_Number varchar(12),Name varchar(25),
Mobile_Number varchar(10),Total_Income int,Rate_of_tax float,Income_Tax int);
"""

#<Import Statements>
import pandas as pd
import mysql.connector as msctr
import pymysql
from sqlalchemy import create_engine
#</Import Statements>

#Connecting to Database
con=msctr.connect(host="localhost",user="root",passwd="12345",database="ITCMS")
dfts=pd.read_sql("SELECT * FROM Taxslab;",con)

if con.is_connected():
    print()
    print("Successful connection to MySQL Database")

print()
print("------------------------------------------------------------------------------------------------------------------")
print()
print("INCOME TAX CALCULATION MANAGEMENT SYSTEM")
print()

#Defining fuctions calculator can do
n='n'
while n=='n':
    print("\t\t\tWhat Do you Want to do : ")
    print()
    print("\t1. Calculate Income Tax and Display Report - \tEnter 1 ")
    print()
    print("\t2. View Tax Slabs - \t\t\t\tEnter 2 ")
    print()
    print("\t3. Display Already Calculated Income Taxes - \tEnter 3 ")
    print()
    print("\t4. See what Tax Slab you Come under - \t\tEnter 4")
    print()
    
    f=int(input('Enter the corresponding number to one of the above functions : '))
    
    if f==1:
        print()
        #Inputting Data for Taxpayer
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
        taxpayer=pd.DataFrame(columns=("PAN_number","Aadhar_Number"\
                                       ,"Name","Mobile_Number","Total_Income","Rate_of_tax",\
                                          "Income_Tax"))
        
        taxpayer.at[0]=[PAN,aadhar,name,mobileno,income,rate*100,tax]
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
        print("Total Income during the year :   \t",income)
        print()
        print("Rate of Taxation : \t\t\t",rate*100,"%")
        print()
        print("Amount of Income tax to be paid :\t",tax)
        print()
        print("-------------------------------------------------------------------------------------------------------------------")
    
        #Code to export the Taxpayer DataFrame to MySQL
        dbengine=create_engine('mysql+pymysql://root:12345@localhost/ITCMS')
        connn=dbengine.connect()
        taxpayer.to_sql('taxpayer',connn,index=False,if_exists='append')
        connn.close()
    
    elif f==2:
        print()
        #Displaying Tax Slabs
        print("\t\t\tTax Slabs Are : ")
        print()
        print(dfts)
    
    elif f==3:
        print()
        #Displaying taxpayer Table from SQL
        pd.set_option('display.expand_frame_repr', False) #Preventing from bad display
        taxpr=pd.read_sql("SELECT * FROM taxpayer;",con)
        print("\t\t\tPreviously calculated Income Tax Data Is : ")
        print()
        print(taxpr)
    
    elif f==4:
        print()
        #Displaying Tax Slabs and rate
        income=int(input('Enter your Annual Income : '))
        print()
        if income<=250000:
            rate=dfts.mrate[0]
            print("\tYou come under 1st Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>=250001 and income<=500000:
            rate=dfts.mrate[1]
            print("\tYou come under 2nd Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>=500001 and income<=750000:
            rate=dfts.mrate[2]
            print("\tYou come under 3rd Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>=750001 and income<=1000000:
            rate=dfts.mrate[3]
            print("\tYou come under 4th Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>=1000001 and income<=1250000:
            rate=dfts.mrate[4]
            print("\tYou come under 5th Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>=1250001 and income<=1500000:
            rate=dfts.mrate[5]
            print("\tYou come under 6th Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
    
        if income>1500000:
            rate=dfts.mrate[6]
            print("\tYou come under 7th Tax Slab")
            print()
            print("\tRate of Taxation for you is :",rate*100,"%")
        print()
    
    else:
        print()
        print()
        print("\t\t\t\t\tInvalid Value")
        print()
        print("\t\t\t\t\tEnter a valid value")
    print()
    print("Enter 'n' if you want to continue")
    print("Enter 'y' if you want to exit")
    n=input('Enter "y" or "n" : ')
    
#Closing Connections to Database
con.close()

print()
print()
print("Thank You for using INCOME TAX CALCULATION MANAGEMENT SYSTEM By Sameer Prasanna")
print()
print()
print("x--------------------------------------------x-----------------------------------------x")
