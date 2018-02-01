# Motzkin tre of size n
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

def test() :
  for n in range(6) :
    print(list(mot(n)))      

import pprint

def test1() :
  for n in range(6) :
    pprint.pprint(list(mot(n)))  