class Solution(object):
    def isValid(self, s):
        opening_brackets = set('({[')
        closing_to_opening = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in opening_brackets:
                stack.append(c)
            else:
                if not stack or stack[-1] != closing_to_opening[c]:
                    return False
                stack.pop()
        return not stack
