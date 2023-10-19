# Author : Sushant
# Project Work : Library Management System
# BASIC COMMAND LINE INTERFACE

# Importing Important Libraries and Modules
import mysql.connector as con
import hashlib # For PASSWORD SECURITY
import pickle as p # in use
from getpass import getpass 
import module1 as m1 # view books & searching
import module2 as m2 # add & remove books
import cdatabase # creates database if not found 
import os

# # Connecting Database
# mydb = con.connect(host='localhost',user='root',password='Home&8296')
# cursor = mydb.cursor()

# ADMIN FUNCTIONALITY [ more features ]
def askadmin():
    'Features only accessible to admin [ requires password ]'
    print('-- ADMIN PANEL --')
    admin_help = 'v > view books \ns > search books \na > add books\nr > remove books\ne > exit'
    print("\nUSE 'H' OR 'h' FOR HELP")

    while True:
        user = input('admin $ ')
        if user == 'v':
            print('')
            rs= m1.viewbooks(userpass)
        elif user=='h':
            print(admin_help)
        elif user == 'a':
            m2.addbooks(userpass)
            pass
        elif user == 'r':
            m2.removebooks(userpass)
            pass
        elif user=='/user':
            user_function()
        elif user == 'e':
            # break
            exit()
        elif user == '':
            pass
        else:
            print('Not Valid Input !')

# USER FUNCTIONALITY [ less features ]
def user_function():
    'Features only accessible to user[ no password required ]'

    print('\nWelcome User')
    user_help = '\nv > view books \ns > search books \ne > exit'
    while True:
        # print('\nv > view books \ns > search books \ne > exit\n')
        user = input('\nuser $ ')
        if user == 'v':
            print('')
            rs= m1.viewbooks(userpass)

        elif user=='/admin':
            ifadmin()
        elif user == 'e':
            # break
            exit()

        elif user.lower()=='h':
            print(user_help)
        
        
        else:
            print('Not Valid Input !')

# Login function for admin panel
def login():
    'asks password from user for admin access'

    # This code checks if admin passoword is setup or not
    # Creates new .dat file for storing hashed password if not found in directory
    print(info)
    print("[ 'E' or 'e' is General exit key ]")
    try:
        f= open('pass.dat','rb')
        global password
        password = p.load(f)
    except:
        askuser = input('Set Password For admin :')
        new_password=hashlib.sha256(askuser.encode('utf-8')).hexdigest() # don't touch this
        f = open('pass.dat','wb+')
        p.dump(new_password, f)
        f.seek(0)
        password = p.load(f)
    finally:
        f.close()

    # Running infinite loop for password value verification until not matched
    while True:
        user = input('\nAdmin ? Y\\n : ')
        user = user.lower()

        # password
        if user=='y':
            ifadmin()
        elif user=='n':
            user_function()

        elif user=='':
            pass

        elif user=='e':
            exit()
        
        else:
            print('Please Choose Accordingly !')

def ifadmin():
    while True:
        ask_pass = input('\nEnter Password: ')
        hashed_password = hashlib.sha256(ask_pass.encode('utf-8')).hexdigest()
        # try:
        #     f.seek(0)
        #     password = p.load(f)
        # except:
        #     pass

        if hashed_password == password:
            askadmin()
            break
        
        elif ask_pass=='':
            pass

        elif ask_pass=='e':
            break

        else:
            print('wrong password')

# General Interface Guide 
# print('_'*42)
info = 'Library Management System [version 1.8]\n(c) Sushant. All rights reserved\n'
print(info)

# Runs 3 times to take and match mysql password for further processing 
for i in range(3):
    userpass = input('Enter your mysql password : ')
    i +=1
    if i>=3:
        print('Try Again ! ')
        break
    try:
        mydb = con.connect(host='localhost',user='root',password=userpass)
        # print('success')
        print('\nSUCCESSFULLY LOGINED..')
    except:
        print('wrong password')
    else:
        cdatabase.createdatabase_if_not(userpass)
        js = input('Enter To Continue....')
        os.system('cls')
        login() # Calling login function only if the password is matched 