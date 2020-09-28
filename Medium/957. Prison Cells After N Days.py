class Solution:
    def prisonAfterNDays(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        catch = []
        while k and nums not in catch:
            t = nums[:]
            catch += nums[:],
            for i in range(1, len(nums) - 1):
                if t[i - 1] == t[i + 1]:
                    nums[i] = 1
                else:
                    nums[i] = 0
            k -= 1
            nums[0] = 0
            nums[-1] = 0
        if catch[0][0] == 1 or catch[0][7] == 1:
            catch = catch[1:]

        if not k or not catch:
            return nums

        return catch[k % len(catch)]
