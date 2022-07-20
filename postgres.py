import psycopg2
import os
import util

util.set_environ_vars()


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
    db = os.environ.get('PGDBNAME')
    user = os.environ.get('PGUSER')
    pwd = os.environ.get('PGPASSWORD')
    host = os.environ.get('PGHOST')
    port = os.environ.get('PGPORT')
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


if __name__ == '__main__':
    # db = os.environ.get('PGDBNAME')
    # user = os.environ.get('PGUSER')
    # pwd = os.environ.get('PGPASSWORD')
    # host = os.environ.get('PGHOST')
    # port = os.environ.get('PGPORT')
    # connectDB(db, user, pwd, host, port)

    # create table function test
    createTable()
