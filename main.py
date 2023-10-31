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
import module3 as m3
import cdatabase # creates database if not found 

# Connecting Database
# mydb = con.connect(host='localhost',user='root',password='Home&8296')
# cursor = mydb.cursor()

# ADMIN FUNCTIONALITY [ more features ]
def admin_function():
    'Features only accessible to admin [ requires password ]'
    print('-- ADMIN PANEL --')
    bookhelp = '\nv > view books \ns > search books \na > add books\nu > update books\nr > remove books\nm > manage books\n'
    print("\nUSE 'H' OR 'h' FOR HELP")
    while True:
        user= input('admin $ ')
        user = user.strip()
        user = user.lower()
        if user== 'h':
            print(bookhelp)
        elif user=='v':
            m1.viewbooks(userpass)
        elif user=='s':
            m1.searchbooks(userpass)
        elif user == 'a':
            m2.addbooks(userpass)
        elif user == 'u':
            m3.updatebooks(userpass)
        elif user == 'r':
            m2.removebooks(userpass)
        elif user == 'm':
            m1.viewissue(userpass)
            m3.managebooks(userpass)
        elif user == 'e':
            break
            # exit()
        elif user == '':
            pass
        else:
            print('Not Valid Input !')

# USER FUNCTIONALITY [ less features ]
def user_function():
    'Features only accessible to user[ no password required ]'

    print('-- USER PANEL --')
    user_help = '\nv > view books \ns > search books \ne > exit'
    print("\nUSE 'H' OR 'h' FOR HELP")
    while True:
        # print('\nv > view books \ns > search books \ne > exit\n')
        user = input('\nuser $ ')
        if user == 'v':
            print('')
            m1.viewbooks(userpass)

        elif user == 'e':
            break
        elif user == 's':
            m1.searchbooks(userpass)

        elif user.lower()=='h':
            print(user_help)
        
        else:
            print('Not Valid Input !')

# Login function for admin panel
def login():
    'asks password from user for admin access'

    # This code checks if admin password is setup or not
    # Creates new .dat file for storing hashed password if not found in directory
    # print(info)
    # print("\n[ 'E' or 'e' is General exit key ]")
    try:
        f= open('lmsdata.dat','rb')
        # global password
        password = p.load(f)
    except:
        askuser = input('Set Password For admin :')
        new_password=hashlib.sha256(askuser.encode('utf-8')).hexdigest() # isko mat chuna
        f = open('lmsdata.dat','wb+')
        p.dump(new_password, f)
        f.seek(0)
        password = p.load(f)
    finally:
        f.close()

    # Running infinite loop for password value verification until not matched
    print("\n[ 'E' or 'e' is General exit key ]")
    while True:
        user = input('\nAdmin ? Y\\n : ')
        user = user.lower()

        # password
        if user=='y':
            while True:
                ask_pass = input('\nEnter Password: ')
                hashed_password = hashlib.sha256(ask_pass.encode('utf-8')).hexdigest()
                # try:
                #     f.seek(0)
                #     password = p.load(f)
                # except:
                #     pass

                if hashed_password == password:
                    admin_function()
                    break
                
                elif ask_pass=='':
                    pass

                elif ask_pass=='e':
                    break

                else:
                    print('wrong password')

        elif user=='n':
            user_function()

        elif user=='':
            pass

        elif user=='e':
            exit()
        
        else:
            print('Please Choose Accordingly !')

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
        # js = input('Enter To Continue....')
        login() # Calling login function only if the password is matched 


# # bypass
# userpass = 'Home&8296'
# cdatabase.createdatabase_if_not(userpass)
# print('SUCCESSFULLY LOGINED..')
# # js = input('Enter To Continue....')
# admin_function()
# # login()