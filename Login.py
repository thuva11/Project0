from ast import Break
from Function import * 
from Connectionfile import *
from MySQLdb import DatabaseError
from tqdm import tqdm
import time
import mysql.connector
from mysql.connector import (connection)
import pyfiglet
import colorama
from datetime import date
from tabulate import tabulate
import pandas as pd
import csv
import time
import datetime
import sys
import mysql.connector as sql

colorama.init()
Datetoday = date.today() 
currentDate=datetime.datetime.now().date()
hour= datetime.datetime.now().hour   # the current hour
minute= datetime.datetime.now().minute
Dateandtime=str(currentDate) + "-"+ str(hour)+ "-" +str(minute)
usernameA= ("")
PasswordA= ("")
un=()
up=()

##################################################################################################3

connectList = Connect.connection()
obj = Queries(connectList[0], connectList[1])

obj1 = LoginSignup(connectList[0], connectList[1]) #LoginAnd Signup Function
userinput= obj1.LoginAndSignuo() 
 
 
        
if userinput == 2:
    exec(open('D:\Revature\Project0\AccountOpen.py').read()) 
        
elif userinput == 1:
    print('\n------------------------------------------------------------------------------------------------------------')
    usernameA= input("Enter your Username  :  ")
    print('------------------------------------------------------------------------------------------------------------ \n')

    print('------------------------------------------------------------------------------------------------------------')
    PasswordA= input("Enter your Password  :  ")
    print('------------------------------------------------------------------------------------------------------------ \n')

    #connectList = Connect.connection()
    #obj = Queries(connectList[0], connectList[1])

    UserInputTo= obj.CheckLogin(usernameA,PasswordA)
   
while True:
                  
    try:
    
        if UserInputTo == 1:
 
           
            useri= obj1.AfterLoginHome() 

            
             
            if useri == 1: #Deposit 
                for i in tqdm (range (50),
                        desc="Deposit Page loading.....",
                        ascii=False, ncols=75):
                        time.sleep(0.01)
                try: 
                    #obj = Queries(connectList[0], connectList[1])
                    Fetched2= obj.FetchedTitleVariables(usernameA,PasswordA) 
                     
                   
                    for x in Fetched2:
                        print('\n------------------------------------------------------------------------------------------------------------')
                        print("Name : "+  x[0] + " " + x[1]+ "--------------- Acc No : "+str(x[2]) +"------------- Available Balance : "+ str(x[3]) + "USD-----------")
                        print('------------------------------------------------------------------------------------------------------------ \n')



                    DAmount= input("Enter Deposit Amount : ")
                    print('\n')
                    
                    AccNumFromQuery =obj.GetAccNumber(usernameA,PasswordA) 
                    CurrentBalance =obj.GetCurBalance(usernameA,PasswordA) 
              

                    try:
                        Type = "Deposit"
                        UpdatedBalance= float(DAmount)+float(CurrentBalance)
                        #print("Updated balance is : "+ str(UpdatedBalance))
                        obj.UpdateBalanceToAcc(UpdatedBalance,AccNumFromQuery) 
                        obj.UpdateTransTable(Type, Datetoday ,DAmount, AccNumFromQuery)

                        print('\n------------------------------------------------------------------------------------------------------------')
                        print ("----------------------Deposit Sucess!!! Your Available balance is " + str(round(UpdatedBalance,2))+"USD.-------------------------------")
                        print('------------------------------------------------------------------------------------------------------------')
                        #UserInputTo == 1
                       # useri= obj1.AfterLoginHome()
                    except mysql.connector.Error as e:
                        print(e)
                except mysql.connector.Error as e:
                        print("Error "+e)

            elif useri ==2 :
                for i in tqdm (range (50),
                        desc="Withdrawal Page loading.....",
                        ascii=False, ncols=75):
                        time.sleep(0.001)
                try: 
                     
                    Fetched2= obj.FetchedTitleVariables(usernameA,PasswordA) 
                    for x in Fetched2:
                        print('\n------------------------------------------------------------------------------------------------------------')
                        print("Name : "+  x[0] + " " + x[1]+ "--------------- Acc No : "+str(x[2]) +"------------- Available Balance : "+ str(x[3]) + "USD-----------")
                        print('------------------------------------------------------------------------------------------------------------ \n')



                    DAmount= input("Enter Withdrawal Amount : ")
                    print('\n')
                    AccNumFromQuery =obj.GetAccNumber(usernameA,PasswordA) 
                    CurrentBalance =obj.GetCurBalance(usernameA,PasswordA) 
                    
                   
                    MinusDamount= -1 * float(DAmount)
                    #print('This is minus : '+ str(MinusDamount))
                    try:
                        UpdatedBalance= float(CurrentBalance) -float(DAmount)
                        if UpdatedBalance >0:
                            #print("Updated balance is : "+ str(UpdatedBalance))
                            obj.UpdateBalanceToAcc(UpdatedBalance,AccNumFromQuery) 
                            
                            
                            try:
                                Type = "Withdrawal"
                                today = date.today()  
                                obj.UpdateTransTable(Type, today ,MinusDamount, AccNumFromQuery)
                            except mysql.connector.Error as e:
                                print("Error "+e)  


                            
                            print('\n------------------------------------------------------------------------------------------------------------')
                            print ("----------------------Withdrawal Sucess!!! Your Available balance is " + str(round(UpdatedBalance,2))+"USD.-------------------------------")
                            print('------------------------------------------------------------------------------------------------------------')
                          
                        else:
                            print('------------------------------------------------------------------------------------------------------------')
                            print ("------------------------------Insufficient balance!!!!.-----------------------------------------------------")
                            print('------------------------------------------------------------------------------------------------------------')
                            Cont=input("Press 0 to User Home : " )
                            Break
                            if Cont ==0:
                                continue 
                             
                    except mysql.connector.Error as e:
                        print(e)
                except mysql.connector.Error as e:
                        print("Error "+e)

            elif useri ==3 : #View Statement
                
                AccNumFromQuery =obj.GetAccNumber(usernameA,PasswordA)
                TransTable =obj.GetTranTable(AccNumFromQuery)
                print(tabulate(TransTable, headers=['TransID', 'Type' ,'Date','Amount'], tablefmt='psql'))
                Cont=input("Press 0 to User Home : " )
                Break
                if Cont ==0:
                        continue
            elif useri == 4: #Generate Statement
                #AccountNumQuery="select a.AccountNum from customers as c  INNER JOIN login as l on c.CustomerID=l.CustomerID  INNER JOIN  accounts as a on  c.SSN=a.SSN where l.Username=%s and l.Passwords=%s"
                AccNumFromQuery =obj.GetAccNumber(usernameA,PasswordA)
                TransTable =obj.GetTranTable(AccNumFromQuery)
               
                
                try:
                    with open('d:/Revature/Project0/ExportCSV/Transaction %s.csv' % Dateandtime,'w') as f:
                        writer = csv.writer(f)
                        writer.writerow({'TransID':'t', 'TransType':'TT', 'Date':'d','Amount':'a'})
                        for row in TransTable:
                            writer.writerow(row)
                    for i in tqdm (range (50),
                        desc="Your Statement Generated Succesfully, Plese Check in d:/Revature/Project0/ExportCSV",
                        ascii=False, ncols=75):
                        time.sleep(0.01)
                    Cont=input("Press 0 to User Home : " )
                    Break
                    if Cont ==0:
                        continue
                except:
                    print("Oops!", sys.exc_info()[0], "occurred.")

            elif useri ==5: #Delete Complete Row 
                
                ans=input("Are You Sure Want to Close your Account (Type Y or y) :" )
                if ans == 'y' or ans =="Y":
                    obj.CloseAccount(usernameA,PasswordA)  
                    print("Thank you for Choosing us. Your Account was Closed Now, Your Available Balance will be Mail as Cheque") 
                    exit()
                else:
                    print("Thank you!") 
                 

                     
        elif UserInputTo== 0: #Incorrect Password
            print("Incorrect Credential Try again") 
                    
            exec(open('D:\Revature\Project0\Login.py').read())
    except mysql.connector.Error as e:
            print(e)


   

