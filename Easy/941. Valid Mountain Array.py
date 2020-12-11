class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        n = len(A)
        i = 0
        while i < n-1 and A[i+1] > A[i]:
            i += 1

        if i == 0 or i == n-1:
            return False

        while i < n-1 and A[i+1] < A[i]:
            i += 1

        return i == n-1

    #dec 10 - 2020
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        def go(arr, val):
            if not arr:
                return True
            if arr[-1] >= val:
                return False
            x = arr.pop()
            return go(arr, x)

        i = arr.index(max(arr))
        l = arr[:i]
        r = arr[i + 1:][::-1]
        if not l or not r:
            return False
        return go(l, arr[i]) and go(r, arr[i])
