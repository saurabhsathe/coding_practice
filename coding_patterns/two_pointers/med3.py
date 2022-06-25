"""

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


Example 2:
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]



"""



def solution(nums,target):
    count=0
    nums.sort()
    for i in range(0,len(nums)-2):
        left=i+1
        right=len(nums)-1

        while left<right:
            curr_sum=nums[i]+nums[left]+nums[right]
            
            
            
            if  curr_sum<target:
                count+=right-left
                left+=1
                
            elif curr_sum>=target:
                right-=1
    return count


print(solution([-1, 0, 2, 3],3))
print(solution([-1, 4, 2, 1, 3],5))





