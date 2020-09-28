class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        letters = []
        for i in range(len(S)):
            if S[i].isalpha():
                letters.append(S[i])
                S[i] = 0
        for i in range(len(S)):
            if S[i] == 0:
                S[i] = letters.pop()

        return ''.join(S)
