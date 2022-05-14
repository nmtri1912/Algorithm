class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits)
        if r == 1:
            if digits[0] == 9:
                return [1, 0]
            digits[0]+=1
            return digits
        extra = False
        for i in range(r - 1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                extra = False
                break
            digits[i] = 0
            extra = True
        if extra == True:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
