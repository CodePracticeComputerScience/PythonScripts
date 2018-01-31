from pprint import pprint

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