'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


def solution(nums,k):
    if k>len(nums):
        return 0
    left=0
    total=float("-inf")
    res=float("-inf")
    for left in range(0,len(nums)-k):
        if total==float("-inf"):
            total=sum(nums[left:left+k])
        else:
            total=total-nums[left-1]+nums[left+k-1]
        if total>res:
            res=total
    return res 


print(solution([2, 1, 5, 1, 3, 2],3))
print(solution([2, 3, 4, 1, 5],2))

