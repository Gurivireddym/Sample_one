def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    return a,b
x=int(input("first number: "))
y=int(input("Second number: "))
print("Before swap:")
print("First number= {} , Second number= {}".format(x,y))
x,y=swap(x,y)
print("After swap:")
print("First number= {} , Second number= {}".format(x,y))