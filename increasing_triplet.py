# Given an unsorted array return whether an increasing
#  subsequence of length 3 exists or not in the array.

import sys
def increasingTriplet(nums):

    mini = sys.maxsize
    maxi = sys.maxsize

    for i in range(1, len(nums)):
        if nums[i] > mini and nums[i] < maxi:
            maxi = nums[i]

        if maxi < nums[i]:
            return True

        if nums[i-1] < nums[i]:
            maxi = nums[i]
            mini = nums[i-1]


    return False




print(increasingTriplet([5,1,5,5,2,5,4]))