import mysql.connector

from connection import connection

class Teacher:
      def __init__(self, id,branch,name,surname,birthdate,gender,ClassId):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        

