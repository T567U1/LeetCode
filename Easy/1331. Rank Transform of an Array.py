class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = { num : i for i, num in enumerate(sorted(set(arr)), start = 1)}
        return [dic[i] for i in arr]
