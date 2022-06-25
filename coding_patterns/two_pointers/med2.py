"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

"""

def solution(nums,target):
    nums.sort()
    max_diff=float("inf")
    for i in range(0,len(nums)-2):
        left=i+1
        right=len(nums)-1
        while left<right:
            diff=target-nums[i]-nums[left]-nums[right]
            if diff==0:
                return target
            
            if abs(diff)<abs(max_diff) or (abs(diff)==abs(max_diff) and diff > max_diff):
                max_diff=diff
            
            if diff>0:
                left+=1
            else:
                right-=1
    
    return target-max_diff











print(solution([-2,0,1,2],2))
print(solution([-3,-1,1,2],1))
print(solution([1,0,1,1],100))







