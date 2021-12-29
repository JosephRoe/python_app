def asal(x,y):
    asal = []
    for i in range(x,y):
        for j in range(2,i):
            if i%j != 0:
                asal.append(i)
    print(asal)

asal(10,24)