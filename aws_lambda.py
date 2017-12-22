import psycopg2
import boto3

def handler(event, context):
    conn_string = "host='<YOUR_DB_HOST>' dbname='<DB_NAME>' user='<DB_USER>' password='<DB_PW>'"
    print(conn_string)

    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("select current_date")
    for r in cur.fetchall():
        print r

