class Solution:
    def fizzBuzz(self, n: int):
        #I think lamba would be faster here??????
        #anyways creates array and past every member by function before adding it
        n = [self.fizzorfuzz(i) for i in range(1, n + 1)]
        return n
    def fizzorfuzz(self, n: int):
        if not bool(n % 5 or n % 3): return 'FizzBuzz'
        elif not bool(n % 5): return 'Buzz'
        elif not bool(n % 3): return 'Fizz'
        else: return n


c = Solution()
print(c.fizzBuzz(16))
