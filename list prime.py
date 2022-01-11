print("Enter List of values separated by space:")
lst=[ int(val) for val in input().split() ]
print("-"*50)
print("\nGiven Numbers={}".format(lst)) # [23, 12, 4, 5, 9, 11, 2, 21,-3, 0, 1]
print("-"*50)
print("Prime Number from Given List:")
for n in lst:
	if(n>1):
		found=True
		for i in range(2,n):
			if(n%i==0):
				found=False
				break
		if(found==True):
			print(n,end=" ")

