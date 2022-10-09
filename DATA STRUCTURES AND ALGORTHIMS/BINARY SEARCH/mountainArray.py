###FUNCTION TO DETERMINE WHETHER AN ARRAY ASCENDS THEN DESCENDS
##Returns true if conditions are met



def mountainArray(arr):                                             #function takes in the array as parameter
    if len(arr) < 3:                                                #condition(if lenght of array is less than three)
        return False                                                #condition returns False if the array size is not three and above
    
    pointer = 1                                                     #points at the second item of the array(for comparison purpose)
    
    ###loop with conditions(checks if the position of the pointer is less than the length of an array)
    #also checks if the item on the pointer is greater than the previous item in the array
    #if true start looping and increase the position of the pointer by one
    while pointer < len(arr) and arr[pointer] > arr[pointer-1]:     
        pointer += 1
        
    ###condition
    #checks if the position of the pointer is still at the sane place(!)
    #checks if the position of the pointer is at the end of the array or at it's final item
    #returns false if conditions are true
    if pointer == 1 or pointer == len(arr):
        return False 
    
    ### another loop with conditions
    #checks if the position of the pointer is less than the length of the array
    #checks if the item on the pointer is less than the previous item in the array
    #if true the pointer increments it's position by one
    while pointer < len(arr) and arr[pointer] < arr[pointer-1]:
        pointer += 1
    
    ##the function returns True if and only if:
    #the pointer is at the same length of the array
    return pointer == len(arr)


#this is the array and should meet the conditions stated above
mount_Arr = [0,1,2,3,4,5,4,3,2,1]
answer = mountainArray(mount_Arr)
print(answer)