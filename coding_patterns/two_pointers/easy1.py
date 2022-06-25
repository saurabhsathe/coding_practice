"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

def solution(nums,target):
    left=0
    right=len(nums)-1

    while left<right:
        if (nums[left]+nums[right])==target:
            return [left,right]
        elif (nums[left]+nums[right])<target:
            left+=1
        else:
            right-=1
    return [-1,-1]


print(solution([1,2,3,4,6],6))
print(solution([2,5,9,11],11))

