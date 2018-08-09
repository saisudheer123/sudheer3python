num1=int(input())
num2=[int(b) for b in input().split()]
s=sorted(num2)
if num1%2==0:
    a=((num1)-1)//2
    b=x+1
    c=(s[a]+s[b])/2
    print(c)
else:
    a=(num1)//2
    print(s[a])
