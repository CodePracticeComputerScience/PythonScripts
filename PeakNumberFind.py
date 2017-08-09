array=[]
for i in range(1000):
    array.append(i)
print ("%s" %(array))

i = 0
#print ("%s" %(len(array)))

while i < len(array):
    #print(i)
    # make sure no index out of range error and verify if last value is peak
    if i == len(array)-1:
        if ( array[i] >= array[i-1] ):
            print("peak value is last element %s" %(array[i]))
            break
    # make sure that if first element is peak then exit on first compare
    if i == 0:
        if  (array[i] >= array[i + 1]) :
            print("peak value is first element %s" %(array[i]))
            print ("%s %s" %(array[i],array[i+1]))
            break
    # compare both side to find peak
    if(array[i] >= array[i - 1] and array[i] >= array[i+1]):
            print("peak value is %s" %(array[i]))
            print ("%s %s %s" %(array[i-1],array[i],array[i+1]))
            #break
      

    i = i + 1






##for item in array:
##    print("%s" % (item))
##    
