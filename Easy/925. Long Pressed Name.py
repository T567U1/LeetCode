class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # what does iter do?????
        typed = iter(typed)
        return all(item in typed for item in name)
