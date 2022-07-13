"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.


"""
def solution(intervals):
    if len(intervals)<=1:
        return intervals
    
    intervals.sort()
    #print(intervals)
    ans=[]
    start=intervals[0][0]
    end=intervals[0][1]

    for i in range(1, len(intervals)):
        #print(start,end)
        if intervals[i][0]<=intervals[i-1][1]:
            start=min(start,intervals[i-1][0])
            end=max(end,intervals[i][1])
        else:
            ans.append([start,end])
            start=intervals[i][0]
            end = intervals[i][1]
       # print(ans)
    ans.append([start,end])
    return ans


print(solution([[1,4], [2,5], [7,9]]))
print(solution([[6,7], [2,4], [5,9]]))
print(solution([[1,4], [2,6], [3,5]]))