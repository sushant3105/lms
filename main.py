# Author : Sushant
# Project Work : Library Management System
# BASIC COMMAND LINE INTERFACE

# Importing Important Libraries and Modules
import mysql.connector as con
import hashlib # For PASSWORD SECURITY
import pickle as p # in use
import module1 as m1 # view books & searching
import module2 as m2 # add & remove books
import cdatabase # creates database if not found 


# # Connecting Database
# mydb = con.connect(host='localhost',user='root',password='Home&8296')
# cursor = mydb.cursor()

# ADMIN FUNCTIONALITY [ more features ]
def askadmin():
    'Features only accessible to admin [ requires password ]'
    print('Welcome To LMS --')
    admin_help = '\nv > view books \ns > search books \na > add books\nr > remove books\ne > exit'
    print("\nUSE 'H' OR 'h' FOR HELP")

    while True:
        user = input('\nadmin $ ')
        if user == 'v':
            print('')
            rs= m1.viewbooks(userpass)
        elif user=='h':
            print(admin_help)
        elif user == 'a':
            m2.addbooks()
        elif user == 'r':
            m2.removebooks()
        elif user == 'e':
            break
        elif user == '':
            pass

        else:
            print('Not Valid Input !')

# USER FUNCTIONALITY [ less features ]
def user_function():
    'Features only accessible to user[ no password required ]'

    print('\nWelcome User')
    while True:
        print('\nv > view books \ns > search books \ne > exit\n')
        user = input('user $ ')
        if user == 'v':
            print('')
            rs= m1.viewbooks(userpass)

        elif user == 'e':
            break

        else:
            print('Not Valid Input !')

# Login function for admin panel
def login():
    'asks password from user for admin access'

    # This code checks if admin passoword is setup or not
    # Creates new .dat file for storing hashed password if not found in directory
    print("\n[ 'E' or 'e' is General exit key ]")
    try:
        f= open('pass.dat','rb')
        # global password
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
print('Library Management System [version 1.8]\n(c) Sushant. All rights reserved\n')

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
        print('successfully logined')
    except:
        print('wrong password')
    else:
        login() # Calling login function only if the password is matched 