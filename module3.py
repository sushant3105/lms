# Update books and Manage

import mysql.connector as con
import module1 as vs
default = 'library'

def updatebooks(sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    mycursor = mydb.cursor()
    # print('[1: bookname | 2: author]')
    # user = input('What do you want to update: ')
    # vs.viewbooks(sqlpass)
    # if user=='1':
    #     user = int(input('enter the serial no :'))
    #     book = input('Enter Book name: ')
    #     mycursor.execute('update books set bookname=%s where srno=%s',(book,user))
    #     mydb.commit()
    # elif user=='2':
    #     user = int(input('enter the serial no :'))
    #     author = input('Enter author name: ')
    #     mycursor.execute('update books set author=%s where srno=%s',(author,user))
    #     mydb.commit()        

    user = input('Enter Serial no: ')
    book = input('Enter Bookname: ').strip()
    author = input('Enter Authorname: ').strip()
    if len(book)>0 and len(author)>0:
        mycursor.execute('update books set bookname=%s,author=%s where srno=%s',(book,author,user))
        mydb.commit()        
    elif len(book)>0 and len(author)==0:
        mycursor.execute('update books set bookname=%s where srno=%s',(book,user))
        mydb.commit()        

    elif len(book)==0 and len(author)>0:
        mycursor.execute('update books set author=%s where srno=%s',(author,user))
        mydb.commit()        
    else:
        print("\n[ /DO YOU MEAN TO ADD BOOKS !? ] [ try 'a' ] ")

def managebooks(sqlpass,dbasename=default):
    pass