### This function will help us find the container that can carry the highest capacity of water
#Finding the maximum area from a given array

from shutil import register_unpack_format


def maxContainer(arr):              ##the function takes an array, the items of the array represent the heights 
    left = 0                        #points the first height of the array
    right = len(arr)-1              #points the last height of the array
    maxArea = 0                     #vairable that stores the maximum area found
    
    while left < right:             #as long as the left pointer's position is less than the right pointer's position-->loop through the array
        maxArea = max(maxArea, min(arr[left], arr[right]) * (right-left))      #finds the maximum value(between the previous calculated maximumArea and the current area )
        
        
        ##we are checking for the maximum height in  this condition 
        if arr[left] < arr[right]:            #as long as the height of the right pointer is greater than the height of the left pointer
            left += 1                         #increment the left pointer by one
        else:                                 #if the right pointer's height is less than the right pointer's height
            right += 1                        #increment the right pointer by one
    
    return maxArea                            #returns the value of the maximum area

heights = [0,1,3,7,3,2,1,8]                   #this is the array containing the heights as it's items
print(maxContainer(heights))                  #call out the functions as the array as it's parameter
        
    