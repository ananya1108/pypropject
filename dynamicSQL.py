import time
import sqlite3
import datetime
import random

conn=sqlite3.connect("dynamicDB.db") #connecting to database 

c=conn.cursor() #cursor created 

def create_table(): #cursor.execute used here
    #dynamic table is created with varname and data type
    c.execute("CREATE TABLE IF NOT EXISTS dynamic(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
    
def dynamic_data_entry():
    unix=int(time.time())
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword='Python'
    value=random.randrange(0,10)

    c.execute("INSERT INTO dynamic (unix, datestamp, keyword, value) VALUES(?,?,?,?)",
              (unix,date,keyword,value))
    conn.commit()

for i in range(10):
    create_table()
    dynamic_data_entry()
    time.sleep(1)

c.close() #cursor cannot be used after this point 
conn.close()    #connection closed
    