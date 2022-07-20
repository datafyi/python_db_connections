import psycopg2
import os
import util

util.set_environ_vars()

db = os.environ.get('PGDBNAME')
user = os.environ.get('PGUSER')
pwd = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')


def get_conn(db, user, pwd, host):
    return psycopg2.connect('dbname={} user={} password={} host={}'.format(db, user, pwd, host))

get_conn(db, user, pwd, host)
print('connection successful...')