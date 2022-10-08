def callBoats(arr, limit):                                      #function to calculate number of boats required
    arr.sort()                                                  #sorts the array in order
    left = 0                                                    #points to the first item of array
    right = len(arr)-1                                          #points to the last item of array
    boats = 0                                                   #number of boats initialized to zero
    
    while left <= right:                                        #as long as the right is greater than the left
        if left == right:                                       #if position of the left is equal to the position of the right
            boats +=1                                           #increment the boats only by one
            break                                               #break the loop completely
        if arr[left] + arr[right] <= limit:                     #if the item on the left pointer + the item on the right pointer is less or equal to the limimt
            left +=1                                            #increment the pos. of left pointer by one
            right -=1                                           #increment position of right pointer by 1
            boats +=1                                           #increase the number of boats needed by one
        if arr[left] == limit:                                  #if the item on left pointer is equal to the limit
            left +=1                                            #increment the position of the left pointer
            boats += 1                                          #increment the boats needed by one
        if arr[right] == limit:                                 #if the item on right pointer is equal to the limit
            right -=1                                           #increment the position of the right pointer
            boats +=1                                           #increment the boats needed by one
    print(f'Sorted array = {arr}\nPosition of left pointer ={left}\nPosition of right pointer= {right}')
    return f'Boats required= {boats}'    

weights = [2,3,1,4,5,1,2]        #array of weights of people to be saved
max_limit = 5                    #the maximum weight the boats can carry

print(callBoats(weights, max_limit))