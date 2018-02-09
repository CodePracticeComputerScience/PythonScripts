#1  1,1,2,3,5,8,13,21,34,55,89,144,..
# def fibo(n) :
#   if n<2 : 
#     return 1
#   else :
#     return fibo(n-2) + fibo(n-1)
# 
# print(fibo(10))
# 
# #2  
# succ = lambda x : x+1  
# print(succ(7))
# 
# #3
# fibo1 = lambda x : 1 if x<2 else fibo1 (x-1) + fibo1(x-2)
# print(fibo1(4))

#4
#def fibo2(n) :
    #i = 1
    #j = 1 
    #k=0
    #or
    #i,j,k = 1,1,0;
    #while(k<n) :
            #ij=i+j
            #i=j
            #j=ij
            #k+=1
            #or
            #ij,i = i+j,j
            #j,k = ij,k+1
    #return i
#print(fibo2(6)) 

#5 returns list 
# def fibos(n) :  
#     def f() :
#         i,j = 0,1
#         k = 0 
#         while(k<n) :
#             k+=1
#             i,j=j,i+j
#             yield i
#     return list(f())
# print(fibos(5)) 

#6 without yield with return
# def fibos1(n) :
#    rs=[]
#    i,j = 0,1 
#    k = 0
#    while(k<n) :
#      k+=1
#      i,j=j,i+j
#      rs.append(i)
#    return(rs)# print(fibos1(5))