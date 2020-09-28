class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if not num:
                if arr.count(0) > 1:
                    return True
                continue
            x = num * 2
            if x in arr:
                print(x, num)
                return True

        return False
