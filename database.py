# creating connection
#---------------------

import mysql.connector
from pickle import TRUE

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
# except:
#     print("connection failed")
#

    
#is_connected() -> to check the connection. return true for success

# print(conn.is_connected()) # checking the connection 
# close()-> close the connection
# conn.close() 
# print(conn.is_connected()) #again checking the connection
    
#cursor()-> contains execute() . so need to create it 

# myc= conn.cursor()
# myc= conn.cursor(buffered=True)
# myc= conn.cursor(prepared=True)

# execute()-> executes the sql query
#cursor object is needed to call execute ()

# close()-> closes the cursor object
# eg. myc.close()



# creating database
#-------------------

# creating cursor object
#myc= conn.cursor() 
# sql for database creation
#sql="CREATE DATABASE pdb"
# executing sql
#myc.execute(sql)
# closing connection
#conn.close()

# to connect to specific database provide database name connection arguments
#-----------------------------------------------------
# ex.
# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
# except:
#     print("connection failed")

# creating table
#-----------------

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#         sql="CREATE TABLE student(stuid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),roll INT,fees FLOAT)"
#         myc=conn.cursor()
#         # myc.execute(sql) # creating tables 
#         myc.execute("SHOW TABLES") # show tables 
#
#         for table in myc:
#             print(table)
#
#         conn.close()
#
#
# except:
#     print("connection failed")



# inserting rows in table
#------------------------

# commit()-> every time you have to call commit() to change the row data inside tables 
#rollback()-> used to un-save the row if there is error

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#         sql="INSERT INTO student(name,roll,fees) VALUES('Surya',101,10000.52)"
#         myc=conn.cursor()
#         myc.execute(sql)
#         conn.commit()
#         print("data inserted..")
#         myc.close()
#         conn.close()
# except :
#     print("data insertion failed")


# rowcount
#---------
# eg. cursor_object.rowcount

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#         sql="INSERT INTO student(name,roll,fees) VALUES('Sonam',102,20000.52),('Sunita',103,40000.52),('Sonam',104,50000.52)"
#         myc=conn.cursor()
#         myc.execute(sql)
#         conn.commit()  # committing the data
#         print("data inserted..")
#         print(myc.rowcount," rows inserted.") # counting the inserted rows
#         myc.close() # close the cursor
#         conn.close() #close the connection
# except :
#     print("data insertion failed")


# lastrowid
#-----------
#when you use the auto_increment for id it returns the last row id

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data insertion failed")
#
# try:
#     sql="INSERT INTO student(name,roll,fees) VALUES('Sonam',102,20000.52),('Sunita',103,40000.52),('Sonam',104,50000.52)"
#     myc=conn.cursor()
#     myc.execute(sql)
#     conn.commit()  # committing the change
#     print("data inserted..")
#     print(myc.lastrowid," id inserted.") # counting the inserted rows
#     myc.close() # close the cursor
#     conn.close() #close the connection
# except:
#     myc.rollback() # unsaving the changes

# Deleting data
#----------------
# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data insertion failed")
#
# try:
#     sql="DELETE FROM student WHERE stuid=10"
#     myc=conn.cursor()
#     myc.execute(sql)
#     conn.commit()  # committing the change
#
#     print(myc.rowcount," row Deleted...") # counting the deleted rows
#     myc.close() # close the cursor
#     conn.close() #close the connection
# except:
#     myc.rollback() # unsaving the changes

#updating the rows
#--------------------

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data insertion failed")
#
# try:
#     sql="UPDATE student set fees=200 WHERE stuid=9"
#     myc=conn.cursor()
#     myc.execute(sql)
#     conn.commit()  # committing the change
#
#     print(myc.rowcount," row updated...") # counting the updated rows
#     myc.close() # close the cursor
#     conn.close() #close the connection
# except:
#     myc.rollback() # unsaving the changes

# fetching data
#-------------

#fetchone()

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="SELECT * FROM student"
#     myc=conn.cursor()
#     myc.execute(sql)
#     row=myc.fetchone()
#
#     while row is not None:
#         print(row)
#         row= myc.fetchone()
#         stuid=row[0]
#         name=row[1]
#         roll=row[2]
#         fees=row[3]
#         print(f'stuid={stuid} Name={name} roll={roll} fees={fees}')
#
#
#
#     print(myc.rowcount," row fetched...") # counting the updated rows
# except:
#     conn.rollback()
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


#fetchall 

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="SELECT * FROM student"
#     myc=conn.cursor()
#     myc.execute(sql)
#     rows=myc.fetchall()
#
#     for r in rows:
#         stuid= r[0]
#         name=r[1]
#         roll=r[2]
#         fees=r[3]
#         print(f'stuid={stuid} Name={name} roll={roll} fees={fees}')
#
#
#
#     print(myc.rowcount," row fetched...") # counting the updated rows
# except:
#     conn.rollback()
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


#fetchmany

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="yondhen1",
#         host="localhost",
#         database="pdb",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="SELECT * FROM student"
#     myc=conn.cursor(buffered=True)
#     myc.execute(sql)
#     rows=myc.fetchmany(5)
#
#     for r in rows:
#         stuid= r[0]
#         name=r[1]
#         roll=r[2]
#         fees=r[3]
#         print(f'stuid={stuid} Name={name} roll={roll} fees={fees}')
#
#
#
#     print(myc.rowcount," row fetched...") # counting the updated rows
# except:
#     conn.rollback()
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


# where clause
#--------------

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="SELECT * FROM student WHERE stuid=2"
#     myc=conn.cursor(buffered=True)
#     myc.execute(sql)
#     rows=myc.fetchone()
#
#     while rows is not None:  # if result fetch is single row no need to loop
#         print(rows) # data will be in tuple
#            break
#
#
#     print(myc.rowcount," row fetched...") # counting the updated rows
# except:
#     conn.rollback()
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


# parameterized qurey
# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="INSERT INTO student (name,roll, fees) VALUES(%s,%s,%s)"
#     myc=conn.cursor()
#     # myc.execute(sql,("Sunita",104,4000.0))
#     params=("Sabina",105,6000.0)
#     myc.execute(sql,params)
#     conn.commit()
#
#     print(myc.rowcount," row inserted...") # counting the inserted rows
# except:
#     conn.rollback()
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection

# insert multiple rows
#---------------------
#executemany()-> executes all parameter sequence 

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="INSERT INTO student (name,roll, fees) VALUES(%s,%s,%s)"
#     myc=conn.cursor()
#     # myc.execute(sql,("Sunita",104,4000.0))
#     seq_of_params=[("Jay",106,6000.0),("Krishna",107,6000.0),("Dipak",108,70000.0)]
#     myc.executemany(sql,seq_of_params)
#     conn.commit() #committing the change
#
#     print(myc.rowcount," row inserted...") # counting the inserted rows
# except:
#     conn.rollback() # rollback the changes
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


# user input parametarized Query
#-------------------------------
# insert single row - input from user -Tuple

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# try:
#     sql="INSERT INTO student (name,roll, fees) VALUES(%s,%s,%s)"
#     myc=conn.cursor()
#     # input from users
#     nm=input("Enter name : ")
#     ro=int(input("Enter roll : "))
#     fee=float(input("Enter fees : "))
#     params=(nm,ro,fee)
#     myc.execute(sql,params)
#     conn.commit() #committing the change
#
#     print(myc.rowcount," row inserted...") # counting the inserted rows
# except:
#     conn.rollback() # rollback the changes
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


# user input parametarized Query
#-------------------------------
# insert multiple row - input from user -Tuple

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
# def student_data(n,r,f):
#     try:
#         sql="INSERT INTO student (name,roll, fees) VALUES(%s,%s,%s)"
#         myc=conn.cursor()
#         # input from users
#         name=n
#         roll=r
#         fees=f
#
#         params=(name,roll,fees) # in tuple you have to maintain order of parameter
#        # you can use list of dictionaries but parameter format will be different see documentation(eg.%(name)s)
#         myc.execute(sql,params)
#         conn.commit() #committing the change
#
#         print(myc.rowcount," row inserted...") # counting the inserted rows
#     except:
#         conn.rollback() # Rollback the changes
#         print("unable to fetch data..")
#
#     myc.close() # close the cursor
#     conn.close() #close the connection
#
# while True:
#     nm=input("Enter name : ")
#     ro=int(input("Enter roll : "))
#     fee=float(input("Enter fees : "))
#     student_data(nm,ro,fee)
#     ans=input("Do you want to exit?(y/n)")
#     if(ans=="y"):
#         break


# deletion of rows
#-------------------

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
#
# try:
#     sql="DELETE FROM student where stuid=%s"
#     myc=conn.cursor() 
#
#     n= int(input("input id for delete: "))   
#     del_value=(n,)     
#     myc.execute(sql,del_value)
#     conn.commit() #committing the change
#
#     print(myc.rowcount," row deleted...") # counting the deleted rows
# except:
#     conn.rollback() # Rollback the changes
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection


# update
#---------
# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
#
# try:
#     sql="UPDATE student SET fees=%s WHERE stuid=%s"
#     myc=conn.cursor() 
#
#     stuid= int(input("input id for update: "))       
#     fee= int(input("input fee amount: ")) 
#     myc.execute(sql,(fee,stuid))
#     conn.commit() #committing the change
#
#     print(myc.rowcount," row updated...") # counting the deleted rows
# except:
#     conn.rollback() # Rollback the changes
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection

# update -> user input

# try:
#     conn=mysql.connector.connect(
#         user="root",
#         password="Yondhen1",
#         host="localhost",
#         database="python",
#         port=3306,
#         )
#     if conn.is_connected():
#         print("database connected")
#
# except :
#     print("data failed  failed")
#
#
# try:
#     sql="UPDATE student SET name=%(n)s,roll=%(r)s,fees=%(f)s WHERE stuid=%s"
#     myc=conn.cursor() 
#
#     stuid= int(input("input id for update: "))  
#     nm=input("Enter Name: ")
#     ro= int(input("Enter Roll: "))   
#     fee= int(input("Enter fees: ")) 
#     update_value={'n':nm,'r':ro,'f':fee,'i':stuid}
#     myc.execute(sql,(fee,update_value))
#     conn.commit() #committing the change
#
#     print(myc.rowcount," row updated...") # counting the deleted rows
# except:
#     conn.rollback() # Rollback the changes
#     print("unable to fetch data..")
#
# myc.close() # close the cursor
# conn.close() #close the connection

#fetching parameterizd data
#---------------------------

try:
    conn=mysql.connector.connect(
        user="root",
        password="Yondhen1",
        host="localhost",
        database="python",
        port=3306,
        )
    if conn.is_connected():
        print("database connected")

except :
    print("data failed  failed")


try:
    sql="SELECT * FROM student WHERE stuid=%s"
    myc=conn.cursor() 
    display_value=(7,) # parameter in Tuple
    myc.execute(sql,display_value)
    row=myc.fetchone()
    print(row)
    print(myc.rowcount," row fetched...") # counting the deleted rows
except:
    conn.rollback() # Rollback the changes
    print("unable to fetch data..")

myc.close() # close the cursor
conn.close() #close the connection


