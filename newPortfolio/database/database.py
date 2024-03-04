from peewee import PostgresqlDatabase

db = PostgresqlDatabase('postgres', user='postgres', password='1234', host='localhost', port='5432')
