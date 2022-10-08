#binary search
#use of pointers
#while loops
def binarysearch(arr, target): # this is a function to search for the target in the given array
    
    left = 0    #points to the first item of the array
    right = len(arr)-1 #points to the last item of the array
    
    #loop
    while(left<=right):             #as long as the left pointer is less than or equal to the position of the right pointer
        mid = (left + right)//2     #find the middle item of the array (5/2=2)
        
        if (arr[mid] == target):    #if the middle item is equal to our target
            return mid              #we have found our target stop looping
        elif (arr[mid] < target ):  #if the middle item is less than our target
            left = mid + 1          #take the left pointer to the middle and ignore the items behind it
        else:                       #if the middle item is greater than the target
            right = mid - 1         #take the right pointer to the middle
    return -1                       #if the target is not in the array return -1

arr = [1,2,3,4,5,6]                 #this is the array
target = 1                        #this is our target

result = binarysearch(arr, target)  #this is where we store the result(positiion of the target)

if result != -1:                                        #if the result is not -1(in our array)
    print("Element is present at index %d" % result)    #print the position of our target
else:                                                   #if the result is not in our target(-1)
    print("No such element")                            #print this
    
#The result printed is "Element is present at index 5"
