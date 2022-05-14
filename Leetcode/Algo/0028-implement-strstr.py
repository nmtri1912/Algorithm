class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        l1, l2 = len(haystack), len(needle)
        i = 0
        while i < l1:
            if haystack[i] == needle[0]:
                if i + l2 <= l1 and haystack[i:i+l2] == needle:
                    return i
            i+=1
        return -1
