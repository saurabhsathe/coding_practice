'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''


def solution(fruits):
    if len(fruits)<=2:
        return len(fruits)
    left=right=0
    count={}
    queue=set()
    res=-1
    start=end=0
   
    while right<len(fruits) :
    
        while right<len(fruits):
            if fruits[right] not in queue and len(queue)==2:
                break
            else:
                queue.add(fruits[right])
            
            count[fruits[right]]=count.get(fruits[right],0)+1
            right+=1
        queue.remove(fruits[left])
        if (right-left)>res:
            start=left
            end=right
            res=(right-left)
        curr=fruits[left]
        while count[curr]>0 and left<=right:
            count[fruits[left]]-=1
            left+=1
    print(start,end)
    
    return res

print(solution(['B', 'B', 'B', 'B', 'B', 'B']))

"""
print(solution(['A', 'B',  'C', 'A', 'C']))

print(solution(['A', 'B', 'C', 'B', 'B', 'C']))

print(solution(['A', 'B','A', 'B',  'C', 'A', 'C']))
"""