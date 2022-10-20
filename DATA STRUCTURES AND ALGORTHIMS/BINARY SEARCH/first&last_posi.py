

##Class named search for target that has the functions of searching for the first and last target of the givent array(repeated)
class search_for_target:
    ##!the array must be sorted to perform a bunary search
    
    #function to find the first target of repeated number in a sorted array
    #takes in 3 parameters(self->to refer to object, a sorted array of numbers, and the target)
    def search_for_first_target(self, arr, target):
        left = 0                                        #left pointer , points to the beginning of the array
        right = len(arr)-1                              #right pointer, points to the end of an array
        
        while(left <= right):                           #as long as the left is less than the right pointer loop through the array
            mid = (left + right) // 2                   #find the middle element of the array(position only)
            
            if (arr[mid] == target):                    #if the middle element is equal to the target
                
                #1 if the mid position is at the start of the array 
                #if the pevious element of the mid and as long as the mid position is greater or equal to zero
                if(mid == 0 or arr[mid-1] != target and mid-1 >= 0):
                    #return the mid position
                    return mid 
                #if mid is not equal to target decrement the right pointer
                right = mid-1
            #else if the mid element is greater than the target
            elif(arr[mid] > target):
                #decrement the right pointer from the middle by one
                right = mid-1
            #else increment the position of the left pointer from the middle by one
            else:
                left = mid+1
        #if array doesnt suit conditions return -1
        return -1
    
    #function to searcht for the last repeated target
    #works the same way as the previous function
    def search_for_last_target(self, arr, target):
        left = 0 
        right = len(arr)-1
        
        while(left <= right):
            mid = (left + right) // 2
            
            if (arr[mid] == target):
                if(len(arr)-1 == target or arr[mid+1] != target and mid + 1 <= len(arr)-1):
                    return mid
                left = mid + 1
            elif(arr[mid] > target):
                right = mid - 1
            else:
                left = mid+1
        return -1
                
    #function called search range that takes 3 parameters
    #1->the array, the object name and the target
    def search_range(self, arr, target):
        left = self.search_for_first_target(arr, target)
        right = self.search_for_last_target(arr, target)
        
        #returns alist containing the positions of the first and last search items
        return [left, right]
    
solution = search_for_target()                          #caling the class solution
answer = solution.search_range([1,2,2,2,3,4,5], 2)      #calling the search range function from the search for target class
print(answer)           #prints out the results