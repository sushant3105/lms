# Editing Module
import mysql.connector as con

def addbooks(sqlpass,dbasename='library'):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    srno = int(input('Enter SrNo: '))
    bookname = input('Enter Bookname: ')
    authorname = input('Enter Authorname: ')
    # cursor.execute(f"insert into books value({srno},'{bookname}','{authorname}')")
    cursor.execute("insert into books value(%s,%s,%s)",(srno,bookname,authorname))
    mydb.commit()

def removebooks():
    pass