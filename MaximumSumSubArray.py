

# Max Sum Subarray of size K:
# Problem Statement Link: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        sum, res = 0,0
        i,j = 0,0
        
        while(j<N):
            sum += Arr[j]
            if(j-i+1) < K:
                j+=1
            elif (j-i+1 == K):
                res = max(res,sum)
                sum -= Arr[i]
                i+=1
                j+=1
        return res