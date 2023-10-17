# Creates Database and tables [ at the start ] or [ if not found ]

import mysql.connector as con

def createdatabase_if_not(sqlpass,dbasename='library'):
    # dbasename = input('Enter DATABASE/OR CREATE : ')
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
        mera = mydb.cursor()
    except:
        print('Creating a new one...')
        mydb = con.connect(host='localhost',user='root',password=sqlpass)
        mcursor = mydb.cursor()
        mcursor.execute(f'create database {dbasename}')
        print('\nDATABASE SUCCESSFULLY CREATED ..') 
        mydb.commit()
        # mcursor.execute()
    else:
        print('DATABSE FOUND ..')
        try:
            mera.execute('show tables')
            result = mera.fetchall()
            if len(result)==0:
                createtable()
        except Exception as e:
            print('Error at e ')
            print(e)

    return sqlpass
def createtable():
    print('hello brother')
    # return dbasename

def deletedatabase(sqlpass, dltit):
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dltit)
    except:
        print('No such database found..')
    else:
        mera = mydb.cursor()
        mera.execute(f'drop database {dltit}')
        mydb.commit()
        print('success')
