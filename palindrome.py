sai=int(raw_input())
sum=0
n=sai
while sai!=0:
    rem=sai%10
    sum=sum*10+rem
    sai=sai/10
if sum==n:
    print("yes")
else:
    print("no")
