class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rlist = []
        for i, num in enumerate(nums):
            count = 0
            for j, numt in enumerate(nums):
                if i is j:
                    continue
                if numt < num:
                    count += 1

            rlist.append(count)

        return rlist
