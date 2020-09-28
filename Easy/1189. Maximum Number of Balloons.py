class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballons, ans = [], []
        for letter in 'balon':
            ballons += [letter] * text.count(letter)

        while True:
            ballon = ''
            for letter in 'balloon':
                if letter not in ballons:
                    return len(ans)
                ballon += letter
                ballons.remove(letter)
            ans.append(ballon)
