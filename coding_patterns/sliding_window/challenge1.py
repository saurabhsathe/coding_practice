'''
Problem Challenge 1
Permutation in a String (hard) 
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''


def helper(s,p):
    if len(p.keys())>0:
        for i in p:
            if i not in s or s[i]!=p[i]:
                return False
    return True


def solution(s,p):
    count={}
    for i in p:
        count[i]=count.get(i,0)+1
    patt_len=len(p)
    init_counts={}
    
    for i in range(0,patt_len):
        init_counts[s[i]]=init_counts.get(s[i],0)+1
    #print(init_counts)
    #print(count)

    if helper(init_counts,count):
        return True
    for i in range(1,len(s)-patt_len+1):
        #print(i,s[i],s[i-1],s[i+patt_len-1],init_counts)
        if init_counts[s[i-1]]>1:
            init_counts[s[i-1]]-=1
        else:
            del init_counts[s[i-1]]

        init_counts[s[i+patt_len-1]]=init_counts.get(s[i+patt_len-1],0)+1
        if helper(init_counts,count):
            return True
    return False



    



print(solution("oidbcaf","abc"))
print(solution("odicf","dc"))
print(solution("bcdxabcdy","bcdxabcdy"))
print(solution("aaaaaaaacb","abc"))