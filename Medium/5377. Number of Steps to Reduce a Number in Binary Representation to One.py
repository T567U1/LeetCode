class Solution:
    def numSteps(self, s: str) -> int:
        s_, steps = int(s, 2), 0
        while s_ != 1:
            if s_ % 2 == 0:
                s_ //= 2
            else:
                s_ += 1
            steps += 1

        return steps
