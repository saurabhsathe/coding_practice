"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].

"""

def solution(jobs):
    jobs.sort(key=lambda x :x [0])
    #print(jobs)
    start,end,maxload=jobs[0][0],jobs[0][1],jobs[0][2]

    res=-1
    for i in range(1,len(jobs)):
        #print(i,maxload,jobs[i][1],end)
        if jobs[i][0]<=end:
            #print("here1")
            start=min(start,jobs[i][0])
            end = max(end,jobs[i][1])
            maxload+=jobs[i][2]
        else:
           # print("here2")
            
            res=max(res,maxload)
            start,end,maxload=jobs[i][0],jobs[i][1],jobs[i][2]
    res=max(res,maxload)

    return res

print(solution([[1,4,3], [2,5,4], [7,9,6]]))
print(solution([[6,7,10], [2,4,11], [8,12,15]]))
print(solution([[1,4,2], [2,4,1], [3,6,5]]))



