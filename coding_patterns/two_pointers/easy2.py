"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.


"""

    
    



def solution(nums):
    ans=[]
    nums.sort()
    
    for i in range(0,len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        target=nums[i]*(-1)
        while l<r:
            curr_sum=nums[l]+nums[r]
            if curr_sum==target:
                ans.append([nums[i],nums[l],nums[r]])
                break      
            elif target>curr_sum:
                l+=1
            else:
                r-=1

            if l==i:
                l+=1
            if r==i:
                r-=1
            
    return ans    


print(solution([-3, 0, 1, 2, -1, 1, -2]))
print(solution([-5, 2, -1, -2, 3]))
