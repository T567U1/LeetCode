class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
        }
        stack = []
        try:
            for char in s:
                if stack and parentheses[stack[-1]] == char:
                    stack.pop()
                    continue
                stack.append(char)
        except KeyError:
            return False
        if not stack:
            return True
        else:
            return False

strs = ["(([]){})","{{)}","({)","})","", "()", "()[]{}", "(]", "([)]", "{[]}", "{{{{[[[[(((())))]]]]}}}}"]
cl = Solution()

for str in strs:
    print(cl.isValid(str))
