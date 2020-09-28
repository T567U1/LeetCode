class Solution:
    def compress(self, chars) -> int:
        if not chars: return 0
        li, anchor, ch = [], 0, chars[0]
        # takes the array and creates multiple arrays by elements
        for i,x in enumerate(chars):
            if x != ch:
                li.extend([chars[anchor:i]])
                anchor = i
                ch = x
        li.extend([chars[anchor:]])
        #clear original array, then add from li by taking each array in the
        #array first element plus len of  given array... oof!!
        chars.clear()
        for i in range(len(li)):
            if len(li[i]) > 9:
                t = list([str(i) for i in str(len(li[i]))])
                chars.extend([li[i][0]])
                chars.extend(t)
            elif len(li[i]) > 1:
                chars.extend([li[i][0], str(len(li[i]))])
            else: chars.append(li[i][0])

        return chars

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
c = Solution()
dic  = enumerate(chars, 1)
print(c.compress(chars))
