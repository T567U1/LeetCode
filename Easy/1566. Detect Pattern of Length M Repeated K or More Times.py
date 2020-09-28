class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i, x in enumerate(arr[:-m]):
            if arr[i: i + m] * k == arr[i: i + m * k]:
                return True

        return False
