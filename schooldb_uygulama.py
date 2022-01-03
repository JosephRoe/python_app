import mysql.connector

from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id,studentNumber,name,surname,birthdate,gender,ClassId):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.ClassId = ClassId

