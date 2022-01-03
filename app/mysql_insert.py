import mysql.connector

def inserProduct():
        connection = mysql.connector.connect(
        host = "localhost",  #192.23.45.56
        user ="root",
        password ="Emre.2022",
        database = "node-app")
        
        cursor = connection.cursor()
        
        sql = "INSERT INTO Products(name,price,image,description) VALUES (%s,%s,%s,%s)"
        
        values = ("Samsung S5", 1000, "1.jpg","iyi telefon")
        
        cursor.execute(sql,values)
        
        try:
            connection.commit()
        except mysql.connector.Error as e:
            print("hata: ",e)
        finally:
            connection.close()
            print("database bağlantısı kapandı.")
    
    