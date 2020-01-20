Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=4.4; b=0.0; c=4.2; y=3.0;
>>> ans=c+a*y*y/b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ans=c+a*y*y/b
ZeroDivisionError: float division by zero
>>> ans=c+(a*y)
>>> 
