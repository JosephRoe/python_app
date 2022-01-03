import json

dict_deneme = {
    
    "name" : "Emre",
    "language": ["Python", "C#"]
    }

result = json.dumps(dict_deneme)

print(result)
print(type(result))
