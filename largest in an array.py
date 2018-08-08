array=[]
num=int(input("no.of:"))
for i in range(1,num+1):
    q=int(input())
    array.append(q)
array.sort()
print("Largest:",array[num-1])
