class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        a, s = float('-inf'), []
        for v in nums[::-1]:
            #print(v < a, a, v)
            #when a is not inf
            if v < a:
                return True
            if s and v > s[-1]:
                while s and s[-1] < v:
                    a = s.pop()
            s += v,
        return False
