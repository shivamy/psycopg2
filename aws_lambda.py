import psycopg2

# lambda handler
def handler(event, context):
    try:
        conn_string = "host='<YOUR_DB_HOST>' dbname='<DB_NAME>' user='<DB_USER>' password='<DB_PW>'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        cur.execute("select current_date")
        for r in cur.fetchall():
            print ("\n{}\n".format(r))
    except Exception as exp:
        print("Unable to connect to database: {}".format(exp))
        
    return("Successfully connected")
