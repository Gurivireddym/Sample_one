Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n=4
>>> def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n

>>> factorial(n)
24
>>> def sumN(n):
    if n == 1:
        return 1
    return sumN(n-1) + n

>>> sumN(4)
10
>>> 
clear
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    clear
NameError: name 'clear' is not defined

>>> string='guru'
>>> def reverseString(str):
    return str[-1::-1]

>>> reverseString(string)
'urug'
>>> def alternateCharacters(str):
    return str[::2]

>>> alternateCharacters(string)
'gr'
>>> 
