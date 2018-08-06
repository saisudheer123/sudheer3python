N1,N2=map(int,input().split())
for num in range(N1,N2):
   sum = 0
   temp = num
   order= len(str(num))
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
       if num == sum:
           print(num,end=" ")

