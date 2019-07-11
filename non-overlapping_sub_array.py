# Given an array A of non-negative integers, return the maximum sum of
#  elements in two non-overlapping (contiguous) subarrays, which have 
#  lengths L and M.  (For clarification, the L-length subarray could 
#  occur before or after the M-length subarray.)



def maxSumTwoNoOverlap(A, L, M):
    n = len(A)
    sumL = [0 for i in range(n)]
    sumM = [0 for i in range(n)]

    sum_till_now_L = 0
    sum_till_now_M = 0
    for i in range(n):

        sum_till_now_L += A[i]

        if i < L - 1 :
            continue
        elif i == L - 1 :
            sumL[i] = sum_till_now_L
        else:
            sum_till_now_L -= A[i-L]
            sumL[i] = sum_till_now_L

    for i in range(n):

        sum_till_now_M += A[i]

        if i < M - 1 :
            continue
        elif i == M - 1 :
            sumM[i] = sum_till_now_M
        else:
            sum_till_now_M -= A[i-M]
            sumM[i] += sum_till_now_M

    
    final_max= 0
    # this is for the L and M

    for i in range(n): 
        max_till_now = 0
        for j in range(n):
            if (j >= 0 and j < i -L) or (j >= i + M):
                max_till_now  = max(sumL[i] + sumM[j], max_till_now)


        final_max = max(final_max, max_till_now)

    return final_max   

        
        
print(maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1,2))


        

