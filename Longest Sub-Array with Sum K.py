# Problem: Longest Sub-Array with Sum K
# Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

# Solution:

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        
        i,j = 0,0
        sm, maxi = 0,0
        
        while j<n:
            sm = sm + arr[j]
            while sm > k and i <= j:
                sm = sm-arr[i]
                i+= 1
            if sm == k:
                maxi = max(maxi, j - i + 1)
                
            j += 1  
                
        return maxi    
    
