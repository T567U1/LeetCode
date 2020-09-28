class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = {i: sum(x) for i, x in enumerate(mat)}
        return sorted(dic, key = dic.get)[: k]
