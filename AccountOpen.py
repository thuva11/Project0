import mysql.connector as sql
from Function import * 
from Connectionfile import *

try:
    uname = input("Create Username :\n")
    passwords =input("Create Password :\n")
    user_fname = input("What is your first name?:\n")
    user_lname =input("What is your last name:\n")
    SSN =int(input("What is your Social Security NO :\n"))
    user_city = input("Your city:\n")
    byear = int(input("Your Birth Year:\n"))
    Mobile = int(input("Your Mobile NO :\n"))

    connectList = Connect.connection()
    obj = Queries(connectList[0], connectList[1])
    obj.InsertQuery(user_fname, user_lname, SSN, user_city, byear,Mobile,uname,passwords) 
    
   
    print('Welcome!!! '+ user_fname + " " + user_lname + ' , Your Account was created Successfully ') 
    exitc =int(input("Press 1 to Back to Home : "))
    if exitc == 1:
                print("=========================================== \n Home Page Loading.................\n===========================================")
                exec(open('D:\Revature\Project0\Login.py').read())

    

except :
    print("Spmething Wrong")
    

