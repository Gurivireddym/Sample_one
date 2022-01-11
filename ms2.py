n=int(input())
d=0
b=[]
for i in range(1,n):
    a= int(input())
    b.append(a)
for i in b:
    d=d+i
c=sum(range(1,n+1))-d
print(c)
