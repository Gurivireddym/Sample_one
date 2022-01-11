#bigex1.py
a=int(input("Enter First Number:"))   #  a=100 
b=int(input("Enter Second Number:")) # b=100
c=int(input("Enter Third  Number:"))  # c=100
if((a>b) and (a>c)):
	print("biggest={}".format(a))
if((b>a) and (b>c)):
	print("biggest={}".format(b))
if(c>a) and (c>b):
	print("biggest={}".format(c))
if(a==b) and (b==c) and (a==c):
	print("ALL VALUES ARE EQUAL")