from cdatabase import *
import view_and_search as m1, add_and_remove as m2
import mysql.connector as con

# deletedatabase('Home&8296','library')
# createdatabase_if_not('Home&8296')

while True:
    user = input('# ')
    if user=='a':
        m2.addbooks('Home&8296')
    elif user=='r':
        m2.removebooks('Home&8296')
    elif user=='v':
        m1.viewbooks('Home&8296')
    else:
        break
m1.viewbooks('Home&8296')

mydb = con.connect(host='localhost',user='root',password='Home&8296',database='library')
cursor = mydb.cursor()

try:
    cursor.execute('select * from books order by id desc limit 1')
    idcount = cursor.fetchone()
    print(idcount)
    idcount = int(idcount[4][0])+1
except Exception as e:
    print('error\n',e)

bookid = str(idcount)+'#'+'F'
print(bookid)

# module2.removebooks('Home&8296')