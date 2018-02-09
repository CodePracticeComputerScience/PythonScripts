def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)
      
#alist = [54,26,93,17,77,31,44,55,20]
alist = [3,2,3]
print(quicksort(alist))

#x[1:] meaning
a = [1,5,9,11,2,66]

a[1:]
# [5, 9, 11, 2, 66]
# 
a[:1]
# [1]
# 
a[-1:]
# [66]
# 
a[:-1]
# [1, 5, 9, 11, 2]
# 
a[3]
# 11
# 
a[3:]
# [11, 2, 66]
# 
a[:3]
# [1, 5, 9]
# 
a[-3:]
# [11, 2, 66]
# 
a[:-3]
# [1, 5, 9]
# 
a[::1]
# [1, 5, 9, 11, 2, 66]
# 
a[::-1]
# [66, 2, 11, 9, 5, 1]
# 
a[1::]
# [5, 9, 11, 2, 66]
# 
a[::-1]
# [66, 2, 11, 9, 5, 1]
# 
# >>> a[::-2]
# [66, 11, 5]
# 
# >>> a[2::]
# [9, 11, 2, 66]