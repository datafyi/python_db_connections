import psycopg2
import os
import util

util.set_environ_vars()

def connectDB(dbname, username, password, address, portnum):
    try:
        conn = psycopg2.connect(database=dbname, user=username, password=password, host=address, port=portnum)
        print('Connection successful')
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()

if __name__ == '__main__':
    db = os.environ.get('PGDBNAME')
    user = os.environ.get('PGUSER')
    pwd = os.environ.get('PGPASSWORD')
    host = os.environ.get('PGHOST')
    port = os.environ.get('PGPORT')
    connectDB(db, user, pwd, host, port)