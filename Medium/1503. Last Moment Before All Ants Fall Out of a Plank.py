# problem says the ants reset eachother path when collide
#but is not an issue for the math since step values is
#not being affected, can be ommited pretend they just passed 
#throught eachother
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left = max(left) if left else 0
        right = (n - min(right)) if right else 0
        return max(left, right)
