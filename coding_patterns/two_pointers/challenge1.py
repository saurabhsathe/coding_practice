""""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.


"""



def solution(nums,target):

    nums.sort()

    ans=[]
    count=0
    curr=[]

    left=0
    right=len(nums)-1
    
    """
    [2, 0, -1, 1, -2, 2]

    [-2,-1,0,1,2,2]



    """
    ans=[]
    for i in range(0,len(nums)-3):
        if i>0 and nums[i]==nums[i-1]:
            continue

        for j in range(i+1,len(nums)-2):
            left=j+1
            right=len(nums)-1
            curr_sum=0
            while left<right:
                curr_sum=nums[i]+nums[j]+nums[left]+nums[right]
                if curr_sum==target:
                    ans.append([nums[i],nums[j],nums[left],nums[right]])
                    break
                elif curr_sum<target:
                    left+=1
                else:
                    right-=1
                



    return ans


print(solution([4, 1, 2, -1, 1, -3],1))
print(solution([2, 0, -1, 1, -2, 2],2))
