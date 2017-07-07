Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3 + 4
7
>>> 3 - 12
-9
>>> 3 * 4
12
>>> 12 / 4
3.0
>>> 12 / 5
2.4
>>> 12//5
2
>>> 8  + 2 * 10
28
>>> (8 + 2) * 10
100
>>> 18 /3
6.0
>>> 18 % 4
2
>>> 18 / 4
4.5
>>> 5 * 5 * 5
125
>>> 5 ** 3
125
>>> t = 5
>>> a = 4
>>> t + a
9
>>> 'kp'
'kp'
>>> "kp"
'kp'
>>> kp
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    kp
NameError: name 'kp' is not defined
>>> 'I don't think so'
SyntaxError: invalid syntax
>>> " I don't think so"
" I don't think so"
>>> 'she said " I don't think so"'
SyntaxError: invalid syntax
>>> 'she said " I think so" '
'she said " I think so" '
>>> she said " I think so "
SyntaxError: invalid syntax
>>> 'I don\'t think so'
"I don't think so"
>>> " I don't think so"
" I don't think so"
>>> 'I don't think so "
SyntaxError: invalid syntax
>>> print("Hi")
Hi
>>> print ('C:\pictures')
C:\pictures
>>> print ('c:\pictures\noon')
c:\pictures
oon
>>> print (r'c:\pictures\noon')
c:\pictures\noon
>>> firstName = "kp"
>>> firstName + "pj"
'kppj'
>>> firstname + " pj "
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    firstname + " pj "
NameError: name 'firstname' is not defined
>>> firstname = "kp"
>>> firstname + " pj "
'kp pj '
>>> firstname = "kp"
>>> firstname * 5
'kpkpkpkpkp'
>>> user = "kp pj"
>>> user[0]
'k'
>>> user[3]
'p'
>>> user[-1]
'j'
>>> user[-3]
' '
>>> user[3]
'p'
>>> user[-6]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    user[-6]
IndexError: string index out of range
>>> user[-5]
'k'
>>> user[1]
'p'
>>> user[1:5]
'p pj'
>>> user[:5]
'kp pj'
>>> user[3:]
'pj'
>>> user[:]
'kp pj'
>>> len('user')
4
>>> len("user")
4
>>> len(user)
5
>>> players = [12,13,15,18,39,45]
>>> players[4]
39
>>> players[0]
12
>>> players[2]
15
>>> players[2] = 68
>>> players
[12, 13, 68, 18, 39, 45]
>>> players + [3,8,9]
[12, 13, 68, 18, 39, 45, 3, 8, 9]
>>> players
[12, 13, 68, 18, 39, 45]
>>> players + append(3,8,9)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    players + append(3,8,9)
NameError: name 'append' is not defined
>>> players.append(3,8,9)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    players.append(3,8,9)
TypeError: append() takes exactly one argument (3 given)
>>> players.append(120)
>>> players
[12, 13, 68, 18, 39, 45, 120]
>>> players[:2]
[12, 13]
>>> players[:2] = [0,0]
>>> players
[0, 0, 68, 18, 39, 45, 120]
>>> players[:2] = []
>>> players[:] = []
>>> players
[]
>>>

