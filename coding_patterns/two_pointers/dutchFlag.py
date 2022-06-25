"""

Problem Statement

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

"""

"""
def solution(nums):

    for i in range(0,len(nums)-2):

        left=i
        right=len(nums)-1
        while left<right:
            if nums[left]<nums[i]:
                nums[left],nums[i]=nums[i],nums[left]
            if nums[right]<nums[i]:
                nums[right],nums[i]=nums[i],nums[right]
            left+=1
            right-=1
    return nums
"""
def solution(nums):

    for i in range(0,len(nums)-2):

        left=i
        right=len(nums)-1
        while left<right:
            if nums[left]<nums[i]:
                nums[left],nums[i]=nums[i],nums[left]
            if nums[right]<nums[i]:
                nums[right],nums[i]=nums[i],nums[right]
            left+=1
            right-=1
    return nums









print(solution([1, 0, 2, 1, 0]))
print(solution([2, 2, 0, 1, 2, 0]))



