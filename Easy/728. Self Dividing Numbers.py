class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums_back = []
        for i in range(left, right + 1):
            flag = 1
            for j in str(i):
                if j == '0' or i % int(j) != 0:
                    flag = 0
                    break
            if flag:
                nums_back.append(i)

        return nums_back
                    
