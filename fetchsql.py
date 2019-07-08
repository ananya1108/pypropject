#fetching data from database
import sqlite3

conn=sqlite3.connect("fetching.db")

c=conn.cursor=()

c.execute("SELECT * FROM dynamic(unix,datestamp,keyword,value)")

a=c.fetchall()

for i in a:
    print(i)