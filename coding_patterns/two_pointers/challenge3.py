"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.


"""
def solution(nums):
    start=len(nums)
    end=-1

    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            start=min(start,i)
            end=max(end,i+1)
    
    if end==-1:
        return 0
    
    print(start,end)        
    global_min=float("inf")
    global_max=float("-inf")
    for i in range(start,end+1):
        global_min=min(nums[i],global_min)
        global_max=max(nums[i],global_max)
    i=start
    while i>=0:
        if nums[i]>global_min:
            start=min(i,start)
        i-=1
    i=end
    while i<len(nums):
        if nums[i]<global_max:
            end=max(i,end)
        i+=1
    

    
    print(nums[start:end+1])
    return end-start+1


print(solution([1, 2, 5, 3, 7, 10, 9, 12]))
print(solution([3,2,1]))
print(solution([1,2,3]))
print(solution([1, 3, 2, 0, -1, 7, 10]))

