from Connectionfile import *
from MySQLdb import DatabaseError
from tqdm import tqdm
from mysql.connector import (connection)
import colorama
from datetime import date
from tabulate import tabulate
import pandas as pd
import datetime
import mysql.connector as sql
import pyfiglet

colorama.init()
currentDate=datetime.datetime.now().date()
hour= datetime.datetime.now().hour   # the current hour
minute= datetime.datetime.now().minute
Dateandtime=str(currentDate) + "-"+ str(hour)+ "-" +str(minute)
usernameA= ("")
PasswordA= ("")
un=()
up=()
today = date.today() 
class Queries:

    # parameterized constructor
    def __init__(self, connection, cursor):
        self.curs = cursor
        self.conn = connection

    def InsertQuery(self,user_fname, user_lname, SSN, user_city, byear,Mobile,uname,passwords):
        sql1 = """INSERT INTO customers (FirstName, Lastname, SSN, City,BirthYear,PhoneNo) VALUES ('{}','{}',{},'{}',{},{})""".format(user_fname, user_lname, SSN, user_city, byear,Mobile )
        self.curs.execute(sql1)
        sql2 = """INSERT INTO login (Username, Passwords) VALUES ('{}','{}')""".format(uname, passwords)
        self.curs.execute(sql2)
        sql3 ="""INSERT INTO accounts (SSN) VALUES ({})""".format(SSN )
        self.curs.execute(sql3)
        self.conn.commit()
        # Fetch all the records and use a for loop to print them one line at a time
        #result = self.curs.fetchall()


    def CheckLogin(self,usernameA,PasswordA):
        un=(usernameA,PasswordA,)
        savequery = "select count(FirstName)  from customers as c LEFT JOIN login as l on c.CustomerID=l.CustomerID where l.Username=%s and l.Passwords=%s "
        self.curs.execute(savequery,un)
        Fetched =self.curs.fetchone()[0]
        self.conn.commit()
        return Fetched
    
    def FetchedTitleVariables(self,usernameA,PasswordA):
        un=(usernameA,PasswordA,)
        savequery = "select c.FirstName, c.LastName, a.AccountNum, a.Balance from customers as c  INNER JOIN login as l on c.CustomerID=l.CustomerID  INNER JOIN  accounts as a on  c.SSN=a.SSN where l.Username=%s and l.Passwords=%s"
        self.curs.execute(savequery,un)
        Fetched =self.curs.fetchall()
        self.conn.commit()
        return Fetched


    def GetAccNumber(self,usernameA,PasswordA):
        un=(usernameA,PasswordA,)
        savequery = "select a.AccountNum from customers as c  INNER JOIN login as l on c.CustomerID=l.CustomerID  INNER JOIN  accounts as a on  c.SSN=a.SSN where l.Username=%s and l.Passwords=%s"
        self.curs.execute(savequery,un)
        Fetched =self.curs.fetchone()[0]
        self.conn.commit()
        return Fetched
        
    
    def GetCurBalance(self,usernameA,PasswordA):
        un=(usernameA,PasswordA,)
        savequery = "select a.Balance from customers as c  INNER JOIN login as l on c.CustomerID=l.CustomerID  INNER JOIN  accounts as a on  c.SSN=a.SSN where l.Username=%s and l.Passwords=%s"
        self.curs.execute(savequery,un)
        Fetched =self.curs.fetchone()[0]
        self.conn.commit()
        return Fetched
    
    def UpdateBalanceToAcc(self,UpdatedBalance,AccNumFromQuery):
        savequery = "UPDATE accounts SET Balance = %s WHERE AccountNum =%s"
        self.curs.execute(savequery,[UpdatedBalance, AccNumFromQuery])
        self.conn.commit()
    
    def UpdateTransTable(self, Type, Datetoday ,DAmount, AccNumFromQuery):
        savequery = """INSERT INTO transactions (TransType, Dates, Amount, AccountNumber) VALUES ('{}','{}',{},{})""".format(Type, Datetoday, DAmount, AccNumFromQuery)
        self.curs.execute(savequery)
        self.conn.commit()


    def GetTranTable(self,AccNumFromQuery):
        savequery = "SELECT TransID, TransType, Dates, Amount FROM transactions where AccountNumber = %s"
        self.curs.execute(savequery,[AccNumFromQuery])
        Fetched =self.curs.fetchall()
        self.conn.commit()
        return Fetched 

    def CloseAccount(self,usernameA,PasswordA):
        un=(usernameA,PasswordA,)
        savequery = "DELETE c  from customers as c LEFT JOIN login as l on c.CustomerID=l.CustomerID where l.Username=%s and l.Passwords=%s"
        self.curs.execute(savequery,un)
        self.conn.commit()



class LoginSignup:

    # parameterized constructor
    def __init__(self, connection, cursor):
        self.curs = cursor
        self.conn = connection

    def LoginAndSignuo(self):
        print("1 - Login")
        print("2 - Create Account ")
        IO=self.userinput= int(input("Please Select option :")) 
        return IO

    def AfterLoginHome(self):
            print("Home Page Loading.................\n ===========================================")
            banner1 = pyfiglet.figlet_format("Welcome To ")
            banner = pyfiglet.figlet_format("    NT Bank")
            print(banner1)
            print(banner)
            print("1 - Deposit Money : ")
            print("2 - Withdraw Money :")
            print("3 - View Statement : ")
            print("4 - Generate Statement :")
            print("5 - Close My Account :")
            usernp= self.userinput=int(input("Please Select option : "))
            return usernp