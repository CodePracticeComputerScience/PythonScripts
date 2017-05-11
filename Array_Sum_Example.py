

# Info:

# Author: kp

#declare array
my_array  = [1,3,4,4]

#final count
z=0

print (my_array)

# loop to go over all elements
for i in range(0,len(my_array)):

    #print(my_array[i])

# loop to go over and compare/skip element
    for j in range(0,len(my_array)):
        #skip if same position
        if j == i:
         continue
        else:
            sum = my_array[j] + my_array[i]

            print "i =",i,"j =",j
            print "sum =",sum
            # verify if sum is 8
            if sum == 8:
                z = z + 1

#print it
print "sum of 8 in loop",z ,"times"
