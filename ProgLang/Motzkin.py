#Assignment 1

#Due January 30 at noon, submit via blackboard.

#The folowing Python program generates Motzkin trees (made of leaves, nodes with one branch and nodes with two branches)

# Motzkin tree of size n
from pprint import pprint
def mot (n) :
  if n==0 : 
    yield 'leaf'
  else :
    for m in mot(n-1) :
      yield ('unary',m)
      
    for k in range(0,n-1) :    
      for l in mot(k) :
        for r in mot(n-2-k) :        
          yield ('binary',l,r)


def mot2(n):
    result = []
    if n == 0:
        result.append('leaf')
        return result
    for m in mot2(n-1):
        result.append('unary('+ m +')')
    
    for k in range(0,n-1):    
      for l in mot2(k) :
        for r in mot2(n-2-k) :        
          result.append('binary(' + l + ',' + r +')')
    return result
    
def test() :
  for n in range(6) :
    pprint(list(mot2(n))) 
    
print(test())
'''if __name__ == '__main__':
    test();'''
#Write a program that generates the same output in C/C++ or Java.