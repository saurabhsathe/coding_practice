"""
Problem Statement

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""

def solution(arr1,arr2):
    newlist=[]
    i=j=0
    """
    while i<len(arr1) or j<len(arr2):

        if arr1[i][0]<arr2[j][0]:
            newlist.append(arr1[i])
            i+=1
        elif arr1[i][0]>arr2[j][0]:
            newlist.append(arr2[j])
            j+=1
        else:
            newlist.append(arr1[i])
            newlist.append(arr2[j])
            i+=1
            j+=1
        if i>=len(arr1):
            while j<len(arr2):
                newlist.append(arr2[j])
                j+=1
        if j>=len(arr2):
            while i<len(arr1):
                newlist.append(arr1[i])
                i+=1
        
    print(newlist)
    ans=[]
    start,end=newlist[0][0],newlist[0][1]
    for i in range(1, len(newlist)):
        if newlist[i][0]<=end:
            end=min(newlist[i][1],end)
            start=max(newlist[i][0],start)
        else:
            ans.append([start,end])
            start,end=newlist[i][0],newlist[i][1]

    ans.append([start,end])
    return ans

    """

    i=0
    j=0
    ans=[]
    start,end=arr2[0][0],arr2[0][1]

    while i<len(arr1) and j<len(arr2):
        if arr1[i][0]>=start:
            start=max(start,arr1[i][0])
            end=min(end,arr1[i][1])
            i+=1
        else:
            ans.append([start,end])
            j+=1
            if j<len(arr2):
                start,end=arr2[j][0],arr2[j][1]
            else:
                break
    print(ans)
    return ans


        

    
print(solution([[1, 3], [5, 7], [9, 12]], [[5, 10]]))

#print(solution([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))