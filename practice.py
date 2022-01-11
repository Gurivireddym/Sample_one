
a=500
b=100240.759834772
c='Hello World!'
d=False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print('%i,%.2f,%s,%s'%(a,b,c,d))
s='{0}:{1:d}\t{2} \t {3}\t{4}'.format(d,d,a,b,c)
print(s)
print('%s %s'%(True,False))
print('%i %i'%(True,False))
print()
t=f'{a}{b:,.2f}\n{c[:5]}\n{d}'
print(t)
for i in c:
    if i==" ":
        continue
    elif i=="!":
        break
    else:
        print(i)
values=[3,53,19,-5,60,41,"test,5,22,9,22"]
import copy
a=[[1,1,1,1],[2,2,2,2],[3,3,3,3]]
s_a=copy.copy(a)
d_a=copy.deepcopy(a)
s_a[1][0]=0
d_a[1][0]=99
print(f'original:{a}')
print(f'shallow:{s_a}')
print(f'deep:{d_a}')
print()
print(id(a[1]))
print(id(s_a[1]))
print(id(d_a[1]))
def to_str_fill(i):
    t=str(i).zfill(8)
    return t
s=[x**2 for x in range(10)]
sa=[x for x in s if x%3==0]
[print(x) for x in sa]
