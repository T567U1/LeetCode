class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        ans = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if (arr[i + 1] - arr[i]) != ans:
                return False
        return True
