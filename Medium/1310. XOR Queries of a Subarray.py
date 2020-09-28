class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        for x, y in queries:
            if x > 0:
                ans.append(arr[y] ^ arr[x - 1])
            else:
                ans.append(arr[y])

        return ans
