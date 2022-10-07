
def maxSum(arr, windowsize):                #function that calculate the maximum sum of given window in an arrat(takes 2 parameters.. array and windowsize)
    array_size = len(arr)                   #find the length of the array
    if array_size <= windowsize:            #compare length of array and window size
        print("Invalid Operation")          #print invalid operation if the windowsize is larger
        return -1                           #return -1 and terminate function
    
    window_sum = sum(arr[i] for i in range(windowsize))         #finds the sum of the windowsize in the array
    max_sum = window_sum                                        #saving the maximum sum as the sum gotten above
    
    for i in range (array_size-windowsize):                     #loops through the array confining to the window size
        window_sum = window_sum - arr[i] + arr[i+windowsize]    #eliminates the already counted array item to the left and moves on to the next window size
        max_sum = max(window_sum, max_sum)                      #checks the maximum number (between the window sum calculated and max sum)
        
    return max_sum                                              #returns the maximum sum gotten above

arr = [80, -50, 90, 1]            #this is the array
k=2                                 #this is the window size
answer = maxSum(arr, k)             #this calls out the function and sets its parameters to arr and k and saves it to variable answer
print(answer)                       #prints out the answer


# #####2nd OPTION 
# def maxSum(arr, windowsize):
#     array_size = len(arr)
#     if array_size <= windowsize:
#         return "Invalid Operation"
    
#     window_sum = sum(arr[:windowsize])    #######################changed but same operation
#     max_sum = window_sum
    
    
        
