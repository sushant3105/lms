# Creates Database and tables [ at the start ] or [ if not found ]

import mysql.connector as con

def createdatabase_if_not(sqlpass,dbasename='library'):
    # dbasename = input('Enter DATABASE/OR CREATE : ')
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
        mcursor = mydb.cursor()
    except:
        print('Creating a new one...')
        mydb = con.connect(host='localhost',user='root',password=sqlpass)
        mcursor = mydb.cursor()
        mcursor.execute(f'create database {dbasename}')
        mcursor.execute(f'use {dbasename}')
        print('\nDATABASE SUCCESSFULLY CREATED ..') 
        mydb.commit()
    else:
        print('DATABSE FOUND ..')
    finally:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
        mcursor = mydb.cursor()
        mcursor.execute('show tables')
        result = mcursor.fetchall()
        '''Another Method
        # result = [list(x) for x in result]
        # result = sum(result,[])
        '''
        result =  [element for innerList in result for element in innerList]
        if 'books' and 'manage' in result:
            print('Found Datasets.. ok !')
        else:
            print('Datasets Not Found ')
        

    # return sqlpass

def deletedatabase(sqlpass, dltit):
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dltit)
    except:
        print('No such database found..')
    else:
        mera = mydb.cursor()
        mera.execute(f'drop database {dltit}')
        mydb.commit()
        print(f'SUCCESSFULLY DELETED {dltit}')
