# First negative in every window of size 

def printFirstNegativeInteger( A, N, K):
    # code here
    i,j = 0,0
    neg = []
    res = []
    
    while j< N:
        if A[j] < 0:
            neg.append(A[j])
            
        if(j-i+1) < K:
            j+=1
            
        elif((j-i+1) == K):
            if not neg:
                res.append(0)
            else:
                res.append(neg[0])
                if A[i] == neg[0]:
                    neg.pop(0)
            i+=1
            j+=1
    return res

