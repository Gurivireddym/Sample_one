Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def make_tags(tag,name):
	return "<"+tag+">"+name+"</"+tag+">"

>>> make_tags(i,bye)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    make_tags(i,bye)
NameError: name 'i' is not defined
>>> make_tags('i','bye')
'<i>bye</i>'
>>> 
