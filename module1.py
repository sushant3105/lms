# View & Searching Module

from tabulate import tabulate
import mysql.connector as con

def viewbooks(sqlpass,dbasename='library'):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()

    # infopanel = 'a > all\ng > genre'
    # print(infopanel)
    # user = input('viewbooks $ ')
    cursor.execute('select srno,bookname,author,genre,date from books')
    result = cursor.fetchall()
    # print(len(result))
    result = [list(x) for x in result]

    print(tabulate(result,headers=['Sr no.','Book Name', 'Author ','Genre','Date Added'],tablefmt='simple'))

def searchbooks(sqlpass,dbasename='library'):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    remo = '[1:bookname | 2:authorname]'
    print(remo)
    user = input('What do you want to search -:')
    if user=='1':
        book = input('Enter `bookname` -:')
        cursor.execute('select srno,bookname,author,genre,date from books where bookname=%s',(book,))
    elif user=='2':
        author = input('Enter `author` -:')
        cursor.execute('select srno,bookname,author,genre,date from books where author=%s',(author,))
    else:
        pass

    try:
        result = cursor.fetchall()
        result = [list(x) for x in result]

        print(tabulate(result,headers=['Sr no.','Book Name', 'Author ','Genre','Date Added'],tablefmt='simple'))        
    except Exception as e:
        print(e)
  
if __name__== '__main__':
    # viewbooks('Home&8296')
    searchbooks('Home&8296')