# Creates Database and tables [ at the start ] or [ if not found ]

import mysql.connector as con

def createdatabase_if_not(sqlpass,dbasename='library'):
    # dbasename = input('Enter DATABASE/OR CREATE : ')
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
        mera = mydb.connect()
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
            print('1')
            mera.execute('use library')
            print(2)
            result = mcursor.fetchall()
            print(len(result))
        except Exception as e:
            print('cannot comprehend')
            print(e)
    
    return dbasename

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
