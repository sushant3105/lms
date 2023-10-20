# Creates Database and tables [ at the start ] or [ if not found ]

import mysql.connector as con

def createdatabase_if_not(sqlpass,dbasename='library'): # True values [ already be verified by other funtion ]

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
        createdatasets(sqlpass,dbasename)

    # return sqlpass
def createdatasets(sqlpass,dbasename):
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dbasename)
        mcursor = mydb.cursor()
        mcursor.execute('show tables')
        result = mcursor.fetchall()
        '''Another Method
        # result = [list(x) for x in result]
        # result = sum(result,[])
        '''
        result =  [element for innerList in result for element in innerList]
        if 'books' in result and 'manage' in result:
            print('Found Datasets.. ok !')
        elif 'books' not in result and 'manage' not in result:
            print('\nDatasets Not Found ')
            books = 'srno int,bookname varchar(100),author varchar(100),genre char(4),id char(10),date char(10),primary key(id)'
            manage = 'sr int,issuer varchar(30),bookissued varchar(30)'
            mcursor.execute(f'create table books({books})')
            mcursor.execute(f'create table manage({manage})')
            mydb.commit()
            print('SUCCESSFULLY CREATED DATASETS..')
            print('\n-- READY TO PROCEED --')
        else:
            print('INCOMPLETE TABLE ..\nDELETING DATABASE.. ')
            mcursor.execute(f'drop database {dbasename}')

            createdatabase_if_not(sqlpass,dbasename)


def deletedatabase(sqlpass, dltit):
    try:
        mydb = con.connect(host='localhost',user='root',password=sqlpass,database=dltit)
    except:
        print(f'No such database {dltit} found..')
    else:
        mera = mydb.cursor()
        mera.execute(f'drop database {dltit}')
        mydb.commit()
        print(f'\nSUCCESSFULLY DELETED {dltit}')