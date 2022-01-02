import mysql.connector
import datetime
from connection import connection

class Student:
    
    connection = connection
    mycursor = connection.cursor()
    
    def __init__(self, StudentNumber,Name,Surname,Birthday,Gender):
        self.StudentNumber = StudentNumber
        self.Name = Name
        self.Surname = Surname
        self.Birthday = Birthday
        self.Gender = Gender

    def saveStudent(self)   :
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthday,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = (self.StudentNumber,self.Name,self.Surname,self.Birthday,self.Gender)
        Student.mycursor.execute(sql,values)
        
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as e:
            print("hata: ",e)
        finally:
            Student.connection.close()
            print("database bağlantısı kapandı.")
           
ali = Student("102","Ali","Can",datetime.datetime(2005, 5, 12),"E")

ali.saveStudent()
            
# while True:
    
#     StudentNumber = int(input("Öğrenci numaranızı giriniz :"))
#     Name = input("Adınızı giriniz :")
#     Surname = input("Soyadınızı giriniz :")
#     Birthday =  datetime.datetime(2005, 5, 12)
#     Gender = input("Cinsiyetinizi giriniz :")
    
#     list.append((StudentNumber,Name,Surname,Birthday,Gender))
    
#     result = input('devam etmek istiyor musunuz? (e/h)')
#     if result == 'h':
#         print('Kayıtlarınız veritabanına aktarılıyor...')
#         print(list)
#         insertProducts(list)
#         break
