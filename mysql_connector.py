import mysql.connector
from mysql.connector import connection

connection = mysql.connector.connect(
    
    host = "localhost",  #192.23.45.56
    user ="root",
    password ="Emre.2022",
    # database = "mydatabase"
    database = "schooldb"
        
)

mycursor = connection.cursor()
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE DATABASE myDatabase")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 



    