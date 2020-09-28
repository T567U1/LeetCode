import numpy as np
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = np.array([list(str(num))] * len(str(num)))
        ans_ = []
        for i, num_ in enumerate(str(num)):
            ans[i][i] = '9' if num_ == '6' else '6'
            ans_.append(int(''.join(ans[i])))
        ans_.append(num)
        return max(ans_)
