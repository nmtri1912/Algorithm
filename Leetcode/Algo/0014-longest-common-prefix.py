class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        s_len = len(strs[0])
        for item in strs:
            if(len(item)<s_len):
                s_len = len(item)
        
        for i in range(s_len):
            current_char = strs[0][i]
            for item in strs:
                if(item[i]!=current_char):
                    return prefix
            
            prefix += current_char
        return prefix
        