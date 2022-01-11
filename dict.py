>> d1={10:"apple", 20:"Mango",30:"kiwi"}
>>> print(d1,type(d1))
{10: 'apple', 20: 'Mango', 30: 'kiwi'} <class 'dict'>
>>> print(d1,type(d1),id(d1))
{10: 'apple', 20: 'Mango', 30: 'kiwi'} <class 'dict'> 1672494849664
>>> d1[20]="Sberry"
>>> print(d1,type(d1),id(d1))
{10: 'apple', 20: 'Sberry', 30: 'kiwi'} <class 'dict'> 1672494849664
>>>d1[40]="Guava"