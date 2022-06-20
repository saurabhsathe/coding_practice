'''
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

def solution(s):
    left=right=0
    myset=set()
    res=0
    while right<len(s):

        if s[right] not in myset:
            myset.add(s[right])
        else:
            if (right-left)>res:
                res=right-left
            
            myset=set()
            myset.add(s[right])
            left=right
        right+=1
    
    if len(myset)>res:
        res=len(myset)
    return res 

print(solution("aabccbb"))
print(solution("abbbb"))
print(solution("abccde"))

print(solution("abcaaaaaaaaacde"))
