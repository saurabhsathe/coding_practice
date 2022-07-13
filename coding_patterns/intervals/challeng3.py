"""

For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].
Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].
Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].

Solution

This problem follows the Merge Intervals pattern. Let’s take the above-mentioned example (2) and visually draw it:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]

"""
def solution(intervals):
    ans=[]
    for member in intervals:
        
        for i in range(0,len(member)):
            ans.append(member[i])
    ans.sort(key=lambda x:x[0])

    res=[]
    for i in range(1,len(ans)):
        if ans[i][0]>ans[i-1][1]:
            res.append([ans[i-1][1],ans[i][0]])
    return res







print(solution([[[1,3], [5,6]], [[2,3], [6,8]]]))
print(solution([[[1,3], [9,12]], [[2,4]], [[6,8]]]))
print(solution([[[1,3]], [[2,4]], [[3,5], [7,9]]]))


