##Function that shows all bad functions after the first one
##takes version as it's parameter
def isBadVersion(version):
    firstBad = 5                                        ##FirstBadVersion stored here
    return version >= firstBad                          ##returns true. This makes all the versions after the first one to be a badversion


#Class that holds the function
class Solution:
    
    #function to determine the first bad function
    #takes n as parameter(size of the array given)
    def firstBadVersion(self, n):
        left = 1                                        #points to the 1 index of array
        right = n                                       #points to last index of array

        ##loop (as long as the right pointer is bigger)
        while left < right:                            
            mid = left + (right-left) // 2          #find the mid version
            
            if not isBadVersion(mid):               #if mid version is not a bad version
                left = mid + 1                      #increment the left pointer by one from the mid
            else:
                right = mid                         #else place the right pointer to the mid position
        return left                                 #return left(being the start of the bad versions)
    
s = Solution()
answer = s.firstBadVersion(10)
print(answer)