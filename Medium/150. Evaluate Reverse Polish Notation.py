class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for t in tokens:
            if t.isdigit() or len(t) > 1:#for negative numbers
                ans += t,
            else:
                x = ans.pop()
                y = ans.pop()
                #pops can be move to f function
                #int just to take care of float numbers
                ans += int(eval(f'{y} {t} {x}')),

        return ans.pop()
