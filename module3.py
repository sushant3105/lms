# Update books and Manage

import mysql.connector as con
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
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    mycursor = mydb.cursor()
    print('[1:issue book | 2:return book]')
    remo = input('Enter Choice -:')
    returnd = 'no'
    if remo=='1':
        bookname = input('Book-: ')
        bookname = bookname.capitalize()
        mycursor.execute('select bookname from books')
        result = mycursor.fetchall()

        found = 0        
        for i in result:
            if bookname in i:
                # print('\nBook found')
                found = 1
        if found >=1:
            try:
                username = input('Name-: ')
                mycursor.execute('insert into manage values(%s,%s,%s)',(username,bookname,returnd))
                mydb.commit()
            except:
                print(f'{username} already issued a book')
        else:
            print('book not found')
    elif remo=='2':
        username = input('Name-: ')
        # mycursor.execute("update manage set returned = 'yes' where issuer=%s",(username,))
        mycursor.execute("delete from manage where issuer=%s",(username,))

        mydb.commit()

if __name__=='__main__':
    managebooks('Home&8296')