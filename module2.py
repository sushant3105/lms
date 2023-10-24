# Editing Module
import mysql.connector as con
from datetime import date
default='library'

def addbooks(sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    bookname = input('Enter Bookname: ')
    authorname = input('Enter Authorname: ')
    
    while True:
        genre = input('Genre[NF/F]: ')
        if genre.lower()=='nf' or genre.lower()=='f':
            genre = genre.upper()
            break
        else:
            print('wrong')

    try:
        cursor.execute('select * from books order by srno desc limit 1')
        srno = cursor.fetchone()[0]
        srno = srno+1
    except:
        srno=1

    try:
        cursor.execute('select * from books order by id desc limit 1')
        idcount = cursor.fetchone()
        idcount = idcount[4][0:2]
        idcount = int(idcount)+1
        if len(str(idcount))==1:
            idcount = '0'+str(idcount)
    except Exception as e:
        idcount='01'
    bookid = str(idcount)+'#'+genre
    print(bookid)
    todaydate = str(date.today())

    # cursor.execute(f"insert into books value({srno},'{bookname}','{authorname}')")
    try:
        cursor.execute("insert into books (srno,bookname,author,genre,id,date) values(%s,%s,%s,%s,%s,%s)",(srno,bookname,authorname,genre,bookid,todaydate))
    except Exception as e:
        print('Error at pushing data >>\n',e)
    mydb.commit()

def removebooks(sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    while True:
        try:
            wdel = int(input('Enter srno to delete record: '))
            if isinstance(wdel, int):
                break
        except Exception as e:
            print(e)

    cursor.execute('delete from books where srno=%s',(wdel,))
    cursor.execute('update books set srno=srno-1 where srno>%s',(wdel,))
    mydb.commit()

def removebooks_specified(udao,sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    cursor.execute('delete from books where srno=%s',(udao,))
    # cursor.execute('update books set srno=srno-1 where srno>%s',(udao,))
    mydb.commit()

if __name__=='__main__':
    addbooks('Home&8296')