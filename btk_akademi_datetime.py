import datetime

result = datetime.datetime.now()

simdi = result.year

bugun = datetime.datetime.ctime(simdi)
yarın = datetime.datetime.strftime(simdi,"%Y")

t = "01 Nisan 1985"

dt = datetime.datetime.strptime(t, "%d %B %Y hour")

print(result)
print(bugun)
print(yarın)
print(dt)

