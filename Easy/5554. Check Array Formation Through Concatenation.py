class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for i in arr:
            if not pieces:
                break
            for j, x in enumerate(pieces):
                if x[0] == i:
                    dic[i] = x
                    pieces.pop(j)
                    break

        ans = []
        for i in arr:
            if i in dic:
                ans += dic[i]

        print(ans)
        return ans == arr if arr else 0
