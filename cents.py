# 25, 1,10,5 

# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.
total = 0

def getTotalWays(arr, sum, index):
    if sum == 0:
        # import ipdb;ipdb.set_trace()
        return 1

    if sum < 0:
        return 0
    total  = 0
    for idx, i in enumerate(arr):

        if idx <  index:
            continue

        # if sum-i == 0:
            # print("total", total, "::::sum::", sum, "::i:::", i, "idx::", idx, "::index::", index);
        total += getTotalWays(arr, sum - i, idx)

    return total



def getTotalWaysDP(arr, sum, index):
    
    final = [0]*(sum+1)
    final[0] = 1
    for i in range(1, sum+1):
        ways = 0
        for j in arr:
            try:
                if i >= j:
                    ways +=  final[i-j]
                
            except:
                pass
        try:
            final[i] = ways
        except:
            pass
        
    print(final)
    return final[sum]




if __name__ == "__main__":
    print(getTotalWays([1,5,10,25], 6, 0))





