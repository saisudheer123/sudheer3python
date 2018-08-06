N=int(input())
temp=N
sum=0
while N>0:
    rem=N%10
    sum=rem**3+sum
    N=N//10
if(temp==sum):
    print("yes")
else:print("no")
