class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i, x in enumerate(favoriteCompanies):
            for j, y in enumerate(favoriteCompanies):
                if i == j or len(x) > len(y):
                    continue
                if set(x).issubset(y):
                    break
            else:
                ans.append(i)

        return ans
