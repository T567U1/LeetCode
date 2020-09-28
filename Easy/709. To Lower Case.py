class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(i) + 32) if 'A' <= i <= 'Z' else i for i in str])
