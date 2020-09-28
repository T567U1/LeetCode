class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k >= len(s):
            return s[::-1]
        s, flag = list(s), 0
        for i in range(k, len(s), k * 2):
            s[i - k: i] = s[i - k: i][::-1]

        if i + k < len(s):
            s[i + k:] = s[i + k:][::-1]

        return "".join(s)

        #for index in range(0,len(s),2*k):
	        #s = s[0:index]+s[index:k+index][::-1] + s[index+k:]
        #return s

        #return ''.join(s[i*k:(i+1)*k] if i%2 else s[i*k:(i+1)*k][::-1] for i in range(len(s)//k + 1))
