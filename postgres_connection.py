import psycopg2 as pg

c=pg.connect(database='postgres', user='postgres', password='dev')

print("connection successful")