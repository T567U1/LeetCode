class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        a = []
        ans = []
        for i in nums:
            print(i)
            if a:
                if a[-1] + 1 == i:
                    a += i,
                else:
                    if len(a) > 1:
                        ans += f'{a[0]}->{a[-1]}',
                    else:
                        ans += str(a.pop()),
                    a = [i]
            else:
                a += i,

        if len(a) > 1:
            ans += f'{a[0]}->{a[-1]}',
        else:
            ans += f'{a.pop()}',

        return ans
