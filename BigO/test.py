def solution(arr):
    if len(arr) == 0:
        return ""
    def sumNode(arr, index):
        if index - 1 < len(arr):
            if arr[index - 1] == -1:
                return 0
            return arr[index-1] + sumNode(arr, index *2) + sum(arr, index*2 +1)
        return 0
    
    left = sumNode(arr, 2)
    right = sumNode(arr, 3)
    if left == right:
        return ""
    if left < right:
        return "Right"
    return "Left"
