class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = {}
        for i in range(1, len(searchWord) + 1):
            temp = []
            x = 0
            for word in sorted(products):
                if len(temp) == 3:
                    break
                if word.startswith(searchWord[:i]):
                    temp.append(word)
            ans[searchWord[:i]] = temp

        return ans.values()
