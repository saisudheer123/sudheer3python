x1,x2,x3=map(int,input().split())
if (x1 > x2) and (x1 > x3):
   print(x1)
elif (x2 > x1) and (x2 > x3):
   print(x2)
else:
   print(x3)
