import mysql.connector as con
from datetime import date
default='library'
def addbooks(sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    # while True:
    #     try:
    #         srno = int(input('Enter SrNo: '))
    #         if isinstance(srno, int):
    #             break
    #     except Exception as e:
    #         print(e)

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
    bookid = str(srno)+'#'+genre
    todaydate = str(date.today())

    # cursor.execute(f"insert into books value({srno},'{bookname}','{authorname}')")
    try:
        cursor.execute("insert into books (bookname,author,genre,id,date) values(%s,%s,%s,%s,%s)",(bookname,authorname,genre,bookid,todaydate))
    except Exception as e:
        print(e)
        while True:
            try:
                srno = int(input('Enter SrNo: '))
                if isinstance(srno, int):
                    break
            except Exception as e:
                print(e)
        
    mydb.commit()