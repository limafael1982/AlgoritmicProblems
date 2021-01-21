# solution to the problem "Longest Palindromic Substring".

    
def getSubStr(s, i, j):
    return s[i:j]
    
def expandAroundCenter(s, left, right):
    L = left
    R = right
    si = len(s)
    while (L >= 0 and R < si and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1
    
def longestPalindrome(s: str) -> str:
    if (s is None) or (len(s) < 1):
        return ""
    start = 0
    end = 0
    for i in range(0, len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        leni = max(len1, len2)
        if leni > (end - start):
            start = i - int((leni - 1) / 2)
            end = i + int(leni / 2)
    return getSubStr(s, start, end + 1)

        