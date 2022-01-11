def  findtotal(rno,name,cls,**marks):
	totm=0
	print("-"*50)
	print("Roll Number:{}".format(rno))
	print("Name:{} and Class: {}".format(name,cls))
	print("-"*50)
	for sn,sm in marks.items():
		print("{}--->{}".format(sn,sm))
		totm=totm+sm
	else:
		print("-"*50)
		print("Total marks={}".format(totm))


findtotal(10,"Aditya","X",maths=77,sci=88,soc=66,hindi=88,eng=66)
findtotal(20,"Payal","XII",Maths=99,Phy=58,Che=57)
findtotal(30,"Minakshi","B.Tech",Cm=60,Cpp=70)
