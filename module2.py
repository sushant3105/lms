# Editing Module
import mysql.connector as con

default='library'
def addbooks(sqlpass,dbasename=default):
    mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
    cursor = mydb.cursor()
    try:
        srno = int(input('Enter SrNo: '))
    except Exception as e:
        print(e,'\nOnly Integer allowed')
        srno = int(input('Enter SrNo: '))

    bookname = input('Enter Bookname: ')
    authorname = input('Enter Authorname: ')
    # cursor.execute(f"insert into books value({srno},'{bookname}','{authorname}')")
    cursor.execute("insert into books value(%s,%s,%s)",(srno,bookname,authorname))
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

    cursor.execute('delete from books where sr=%s',(wdel,))
    mydb.commit()
    pass
if __name__=='__main__':
    removebooks('Home&8296')