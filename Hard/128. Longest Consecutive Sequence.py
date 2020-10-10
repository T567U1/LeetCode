class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = []
        while nums:
            c = 0
            head = nums[0]
            while head in nums:
                nums.remove(head)
                head += 1
                c += 1
            ans += c,

        return max(ans)
