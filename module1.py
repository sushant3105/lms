# View & Searching Module

from tabulate import tabulate
import mysql.connector as con

def viewbooks(sqlpass,dbasename='sample'):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    infopanel = 'a > all\ng > genre'
    print(infopanel)
    user = input('viewbooks $ ')
    cursor.execute('select * from books')
    result = cursor.fetchall()
    result = [list(x) for x in result]

    print(tabulate(result,headers=['Sr no.','Book Name', 'Author '],tablefmt='outline'))

def searchbooks():
    
    pass

if __name__== '__main__':
    viewbooks()