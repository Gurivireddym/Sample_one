n=int(input())
b=[]
for i in range(1,n):
    a= int(input())
    b.append(a)
for i in range(1,n+1):
    if(i not in b):
        print(i)
