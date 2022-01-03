import os 
import datetime

def find():
    directory = os.listdir()
    for dosya in directory:
        if dosya.endswith(".py"):
            print(dosya)
            
result = os.stat("btk_akademi.py")

print(datetime.datetime.fromtimestamp(result.st_ctime))
            


