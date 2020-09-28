class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow, powers_of_Twos = 2048, [1,2,4,8,16,32,64,128,256,512,1024,2048]
        if n in powers_of_Twos: return True
        elif n not in powers_of_Twos and n > powers_of_Twos[-1]:
            while pow <= n:
                pow *= 2
                powers_of_Twos.append(pow)
            if n in powers_of_Twos: return True
            else: return False

c = Solution()
print(c.isPowerOfTwo(4096))
