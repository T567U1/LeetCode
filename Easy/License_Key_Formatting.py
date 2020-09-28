class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        #Remove existing '-'
        S, licenseKey_ = S.replace('-', ''), ''
        start = len(S) % K
        #Start: start point for appending string
        if start != 0:
            licenseKey_ += S[:start] + '-'
        #loop for appending string and formatting maybe is fater to change to upper here?
        for i in range(start, len(S), K):
            print(i, start, S, licenseKey_, S[i: i + K])
            licenseKey_ += S[i: i + K] + '-'

        return licenseKey_.upper()[:-1]

c =Solution()
print(c.licenseKeyFormatting("2-5g-3-J", 2))
