n = 100

for i in range(1,n):
  if i % 3 == 0:
    print("Fizz",end=" ")
  elif i % 5 == 0:
    print("Buzz",end=" ")
  elif i % 3 == 0 and i % 5 == 0:
    print("FizBuzz",end=" ")
  else:
    print(i,end=" ")