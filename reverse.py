Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> rev=0
>>> n=int(input("enter a number:\t"))
enter a number:	123
>>> while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n/10

	
>>> rev
inf
>>> while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n/10

	
>>> rev
inf
>>>  while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n//10
	
SyntaxError: unexpected indent
>>> while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n//10

	
>>> rev
inf
>>> rev=0
>>> n=123
>>>  while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n//10
	
SyntaxError: unexpected indent
>>> while(n!=0):
	rem=n%10;
	rev=rev*10+rem
	n=n//10

	
>>> rev
321
>>> rev=0
>>> while(n!=0):
	rem=n%10
	rev=rev*10+rem
	n=n//10

	
>>> rev
0
>>> n=123
>>> while(n!=0):
	rem=n%10
	rev=rev*10+rem
	n=n//10

	
>>> rev
321
>>> 
