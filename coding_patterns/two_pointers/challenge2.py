"""
Problem Statement

Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example 1:

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
Example 2:

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
Example 3:

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
Example 4:

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

"""


def solution(s1,s2):

    left=len(s1)-1
    right=len(s2)-1

    while left>=0 and right>=0:
        count=0
        while left>=0 and s1[left]=="#":
            count+=1
            left-=1
        left=left-count

        count=0
        while right>=0 and s2[right]=="#":
            count+=1
            right-=1
        right=right-count

        
        if s1[left]!=s2[right]:
            return False

        left-=1
        right-=1
    
    return True
    


print(solution("xy#z","xzz#"))
print(solution("xy#z","xyz#"))
print(solution("xp#","xyz##"))
print(solution("xywrrmp","xywrrmu#p"))


