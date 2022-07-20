import psycopg2
import os
import util

util.set_environ_vars()

global db, user, pwd, host, port
db = os.environ.get('PGDBNAME')
user = os.environ.get('PGUSER')
pwd = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')


def connectDB(dbname, username, password, address, portnum):
    conn = None
    try:
        conn = psycopg2.connect(database=dbname, user=username, password=password, host=address, port=portnum)
        print('Connection successful')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def createTable():
    try:
        # Establish connection
        conn = psycopg2.connect(database=db, user=user, password=pwd, host=host, port=port)

        # Create a cursor
        cur = conn.cursor()

        # drop and create employee table
        cur.execute('''DROP TABLE EMPLOYEE''')
        cur.execute('''CREATE TABLE EMPLOYEE \
        ( emp_num int primary key not null,
        emp_name varchar(40) not null,
        department varchar(40) not null
        )''')
        conn.commit()
        print('Table created successfully')
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        cur.close()
        if conn.closed == 0:
            conn.close()


def insertRecord(num,name,dept):
    try:
        conn = psycopg2.connect(database=db, user=user, password=pwd, host=host, port=port)
        cur=conn.cursor()

        cur.execute('''insert into employee(emp_num,emp_name,department) values (%s, %s, %s)''',(num,name,dept))
        conn.commit()
        print('Record successfully inserted')
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if cur.closed==0: cur.close()
        if conn.closed==0: conn.close()


def deleteRecord(num):
    try:
        conn = psycopg2.connect(database=db, user=user, password=pwd, host=host, port=port)
        cur=conn.cursor()
        cur.execute('''delete from employee where emp_num=%s''',(num,))
        conn.commit()
        print('%s row(s) got deleted.' % cur.rowcount)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur.closed == 0: cur.close()
        if conn.closed == 0: conn.close()


def updateRecord(num, dep):
    try:
        conn = psycopg2.connect(database=db, user=user, password=pwd, host=host, port=port)
        cur = conn.cursor()
        cur.execute('''update employee set department = %s where emp_num = %s''',(dep,num))
        conn.commit()
        print('%s record(s) updated.' % cur.rowcount)
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur.closed == 0: cur.close()
        if conn.closed==0: conn.close()

if __name__ == '__main__':
    # db = os.environ.get('PGDBNAME')
    # user = os.environ.get('PGUSER')
    # pwd = os.environ.get('PGPASSWORD')
    # host = os.environ.get('PGHOST')
    # port = os.environ.get('PGPORT')
    # connectDB(db, user, pwd, host, port)

    # create table function test
    createTable()

    #insert record test
    insertRecord(1234,'Roza', 'Civil')
    updateRecord(1234,'IT')
    deleteRecord(1234)