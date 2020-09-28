class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, set_ = [], set(arr1)
        for i in arr2:
            ans.extend([i] * arr1.count(i))
            set_.remove(i)
        if set_:
            for e in sorted(set_):
                ans.extend([e] * arr1.count(e))
        return ans
