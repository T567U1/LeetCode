class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if note bigger than magazine
        if len(ransomNote) > len(magazine): return False
        #letters on magazine no matter as long Note has them
        for i in magazine:
            if len(ransomNote) == 0: return True
            if i in ransomNote:
                ransomNote.remove(i)

        return len(ransomNote) == 0

ransomNote, magazine = "a", 'b'
c = Solution()
print(c.canConstruct(ransomNote, magazine))
