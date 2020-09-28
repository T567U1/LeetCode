class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans, arr = {}, sorted(arr)
        for i in range(len(arr) - 1):
            gap = abs(arr[i] - arr[i + 1])
            if gap in ans:
                ans[gap].append([arr[i], arr[i + 1]])
            else:
                ans[gap] = [[arr[i], arr[i + 1]]]

        return ans[min(ans)]
