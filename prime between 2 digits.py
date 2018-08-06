nm,k=input().split()
nm,k=int(nm),int(k)

for j in range(nm,k):
    count=0
    for i in range(1,j+1):
        if (j%i)==0:
            count+=1
    if(count==2):
        print(j,end=" ")
