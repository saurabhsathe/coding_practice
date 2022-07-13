"""

Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.



"""


def solution(intervals):
    intervals.sort()
    for i in range(1,len(intervals)):
        if intervals[i][0]<intervals[i-1][1]:
            return False
    return True
    

print(solution([[1,4], [2,5], [7,9]]))
print(solution([[6,7], [2,4], [8,12]]))
print(solution([[4,5], [2,3], [3,6]]))
