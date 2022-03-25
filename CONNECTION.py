import psycopg2

conn = psycopg2.connect(dbname='zags', host='10.10.11.30', port='5432', user='postgres', password='!@#QWE123')
cur = conn.cursor()
