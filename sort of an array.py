num1=int(input())
num2=[int(x) for x in input().split()]
S=sorted(num2)
for y in range(num1):
    print(S[y],end=' ')
