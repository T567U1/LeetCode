#"Come back" and make it better and 1000 jokes you tell yourself
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K:
            if min(A) < 0:
                A[A.index(min(A))] = abs(min(A))
                K -= 1
            elif 0 in A:
                break
            else:
                while K:
                    A[A.index(min(A))] *= -1
                    K -= 1

        return sum(A)
