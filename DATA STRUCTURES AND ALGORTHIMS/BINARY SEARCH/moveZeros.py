#How I went about it
## Instead of pushing the zeros to the end, I placed a pointer at the beginning of the array
## moved all the numbers that arent zero to the current positiion of the pointer
## the remaining numbers after the pointer will probably not be zero so you should replace all of them with a zero


def moveZeros(arr):                             #function to move all zeros to the end
    pointer = 0                                 #points to the first item[0] of the array
    length = len(nums)                          #finding the length of the array
    
    for num in nums:                            #loops through the array
        if num!=0:                              #condition (if the item of the array is not zero)
            nums[pointer] = num                 #place the item where the pointer is at the moment
            pointer +=1                         #increment the positiion of the pointer by one and move on to the next
    
    for rest in range(pointer, length):         #loop through the rest of the items(from the last position of the pointer to the length of the array)
        nums[rest] = 0                          #replace the rest of the numbers with zero
    return arr                                  #return the new formatted array
        
nums = [0,1,3,0,3,0,1,3]                        #this is the array we're changing

print(moveZeros(nums))                          #call out the function and place the nums array as the parameter