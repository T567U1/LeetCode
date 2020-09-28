class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = 'aeiouAEIOU'
        S = S.split(' ')
        for i in range(len(S)):
            if S[i][0] in vowels:
                S[i] = S[i] + 'ma' + ''.join(['a' for i in range(i + 1)])
            else:
                S[i] = S[i][1:] + S[i][0] +  'ma' + ''.join(['a' for i in range(i + 1)])

        return ' '.join(S)
