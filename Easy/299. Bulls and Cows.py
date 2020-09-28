class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret, guess = list(secret), list(guess)
        for i, (x, y) in enumerate(zip(secret, guess)):
            if x == y:
                bulls += 1
                secret[i] = "X"
                guess[i] = "X"

        for i in guess:
            if i in secret and i.isdigit():
                cows += 1
                secret.remove(i)

        return "{}A{}B".format(bulls, cows)

c = Solution()
print(c.getHint("121", "110"))
