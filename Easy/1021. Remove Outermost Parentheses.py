class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        ans, temp = "", ""
        for i in S:
            count += 1 if i =='(' else -1
            temp += i
            if count == 0:
                ans += temp[1:-1]
                temp = ""
        return ans
