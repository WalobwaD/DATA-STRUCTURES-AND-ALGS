
def censeq(str):
    left = 0
    right = 0
    m = {}
    answer = 0
    n = len(str)
    
    while left < n and right < n:
        el = str[right]
        if el in m:
            left = max(left, m[el] + 1)
            
        m[el] = right 
        answer = max(answer, right-left + 1)
        right += 1
        
    return answer

s = "abcddeffe"

print(censeq(s))