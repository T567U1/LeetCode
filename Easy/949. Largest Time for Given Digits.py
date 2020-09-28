from itertools import permutations as p
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = []
        nums = p(A, len(A))
        for i in nums:
            hour  = str(i[0]) + str(i[1])
            mins  = str(i[2]) + str(i[3])
            if int(hour) <= 24 and int(mins) < 60:
                add = hour + mins
                if add < '2400':
                    ans += add,

        if ans:
            ans = max(ans)
            return f'{ans[:2]}:{ans[2:]}'
        return ''
