# Find minimum time to finish all jobs with given constraints
# Given an array of jobs with different time requirements. There are K identical assignees available and we are also given how much time an assignee takes to do one unit of the job. Find the minimum time to finish all jobs with following constraints.

# An assignee can be assigned only contiguous jobs. For example, an assignee cannot be assigned jobs 1 and 3, but not 2.
# Two assignees cannot share (or co-assigned) a job, i.e., a job cannot be partially assigned to one assignee and partially to other.
# Input :

# K:     Number of assignees available.
# T:     Time taken by an assignee to finish one unit
#        of job
# job[]: An array that represents time requirements of
#        different jobs.
# Examples :

# Input:  k = 2, T = 5, job[] = {4, 5, 10}
# Output: 50
# The minimum time required to finish all the jobs is 50.
# There are 2 assignees available. We get this time by
# assigning {4, 5} to first assignee and {10} to second
# assignee.

# Input:  k = 4, T = 5, job[] = {10, 7, 8, 12, 6, 8}
# Output: 75
# We get this time by assigning {10} {7, 8} {12} and {6, 8}




def getAvg(arr):
    n = len(arr)
    sum = 0
    max = 0
    for i in arr:
        if max < i:
            max = i
        sum += i
    return sum/n, max


def getMinTime(arr, k, t, breakPoint=0, count=0):
    average, maximum = getAvg(arr)

    if not breakPoint:
        breakPoint = max(average, maximum)
    print("breakpoint: ", breakPoint)

    # if count == k:
    #     print(t)
    #     print(breakPoint)
    #     return breakPoint*t

    # import ipdb; ipdb.set_trace()
    sumTillNow = 0
    maxTillNow = 0
    newBreakPoint = breakPoint;
    count = 0 
    # if breakPoint == 14:
    #     import ipdb;ipdb.set_trace()
    for i in arr:
        sumTillNow += i
        if sumTillNow > breakPoint:
            check = max(breakPoint, sumTillNow)
            if newBreakPoint == breakPoint:
                newBreakPoint = check
            else:
                newBreakPoint = min(newBreakPoint, check)
            
            maxTillNow = max(maxTillNow, sumTillNow - i)
            sumTillNow = i
            count += 1

        if sumTillNow == breakPoint:
            count += 1

    if count > k:
        getMinTime(arr, k, t, breakPoint=newBreakPoint, count=count)
    else:
        print(t)
        print(breakPoint)
        return breakPoint*t


if __name__ == '__main__':
    arr = [10, 7, 8, 12, 6, 8]
    print(getMinTime(arr, 4, 5))



def removeDublicate(string):
    check = 0
    newString = ''
    for i in string:
        if (check & (1 << ord(i)) > 0):
            continue
        else:
            check |= (1 << ord(i))
            newString += i

    return newString
        





