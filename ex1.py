a=10
b=20  # here 'a' and 'b' are called global Variables.
def disp():
	print("Val of a={}".format(a))
	print("Val of b={}".format(b))

def  swapvalues():
	global a,b # refering global variables 'a' and 'b'
	a=a^b
	b=a^b
	a=a^b

#main program
print("Original Values:")
disp()
swapvalues()
print("Swapped Values:")
disp()