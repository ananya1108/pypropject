import sqlite3 #standard sql library already comes with python3

conn=sqlite3.connect("soisIOT.db") #connection object "conn" created that represents the databases,here data will be saved in soisIOT.db

c=conn.cursor() #now you can create a cursos object and call its execution() method to perform SQL methods

#creating table 
def create_table(): #c.execute is also cursor.execute so cursor.execute(sql[,optional parameters])
    c.execute("CREATE TABLE IF NOT EXISTS  ece(unix REAL,datestamp TEXT,keyword TEXT, value REAL)")
    
#inserting rows of data
def data_entry():
    c.execute("INSERT INTO ece VALUES(12345678, '2019-07-05 10:32:50','Python',3)")

#save (commit) the changes.
    conn.commit()
    c.close() #closing the connection 
    conn.close()

create_table() #function call()
data_entry()    
    
    
        