class Solution:
    #catch for values...makes program faster by void repetition
    catche = {
        0 : 0,
        1 : 1,
        2 : 1
    }
    def fib(self, N: int) -> int:
        if N in self.catche:
            return self.catche[N]
        val =  self.fib(N - 1) + self.fib(N - 2)
        self.catche[N] = val
        return val
