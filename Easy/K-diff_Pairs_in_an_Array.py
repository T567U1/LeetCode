class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        #importing Counter from colletction would make this faster but I needed to know what it does
        #conver list to dictionary this will allow us to calculate values faster
        catch = {i : 1 for i in nums}
        count = 0
        if k == 0:
            #count reited numbers
            return len([i for i in set(nums) if nums.count(i) > 1])
        #per item in dictionary plus the target result if in dictionary it woul count + 1
        for i, v in catch.items():
            if i + k in catch:
                count += 1
        return count
