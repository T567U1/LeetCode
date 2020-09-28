#x (Latitude) = moves.count('R') - moves.count('L')
#y (longitude) = moves.count('U') - moves.count('D')
# if those two numbers gives are 0, 0 you are back at base
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return [moves.count('R') - moves.count('L'), moves.count('U') - moves.count('D')] == [0,0]
