# Author : Sushant
# Project Work : Library Management System
# PROFESSIONAL VERSION

import mysql.connector as con
from pyfiglet import Figlet
import hashlib
import pickle as p
import module1 as m1 # view books & searching
import module2 as m2 # add & remove books
import cdatabase

# colors
from termcolor import cprint
import colorama 
colorama.init()


# # Connecting Database
# mydb = con.connect(host='localhost',user='root',password='Home&8296')
# cursor = mydb.cursor()


def askadmin():
    'Features'
    cprint('Welcome To LMS --','yellow')
    admin_help = '\nv > view books \ns > search books \na > add books\nr > remove books\ne > exit'
    cprint("\nUSE 'H' OR 'h' FOR HELP",'white')

    while True:
        cprint('\nadmin $ ','green', end='')
        user = input('')
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
            cprint('Not Valid Input !','red')

def user_function():
    'Features'

    cprint('\nWelcome User','light_blue')
    while True:
        print('\nv > view books \ns > search books \ne > exit\n')
        user = input('user $ ')
        if user == 'v':
            print('')
            rs= m1.viewbooks(userpass)

        elif user == 'e':
            break

        else:
            cprint('Not Valid Input !','red')


def login():
    'login function'
    try:
        f= open('pass.dat','rb')
        # global password
        password = p.load(f)
    except:
        askuser = input('Set Password For admin :')
        new_password=hashlib.sha256(askuser.encode('utf-8')).hexdigest()
        f = open('pass.dat','wb+')
        p.dump(new_password, f)
        f.seek(0)
        password = p.load(f)
    finally:
        f.close()

    while True:
        # cprint('\nAdmin ? Y\\n : ','cyan',attrs=['bold'], end='')
        # user = input('')
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
                    cprint('wrong password','red')

        elif user=='n':
            user_function()

        elif user=='':
            pass

        elif user=='e':
            exit()
        
        else:
            cprint('Please Choose Accordingly !','light_red')


f = Figlet(font='standard')
print(f.renderText('Library Management System'))

print('_'*42)
# print('#'*42)

cprint("\n[ 'E' or 'e' is General exit key ]",'light_yellow')

for i in range(3):
    userpass = input('Enter your mysql password : ')
    i +=1
    if i>=3:
        print('Try Again ! ')
        break
    try:
        mydb = con.connect(host='localhost',user='root',database='sample',password=userpass)
        # print('success')
        print('successfully logined')
    except:
        print('wrong password')
    else:
        login()