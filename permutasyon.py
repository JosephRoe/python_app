import random
import math

a = [1,2,3]

b = []

count = math.factorial(len(a))

while count:
  random.shuffle(a)
  if a not in b: 
    b.append(a[:])
    count -=1

print(b)



