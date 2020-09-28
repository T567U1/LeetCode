class Solution(object):
    def entityParser(self, text):
        translations = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }

        ans = []
        i = 0
        while i < len(text):
            for entity in translations:
                if all(text[i+k] == entity[k] for k in range(len(entity))):
                    ans.append(translations[entity])
                    i += len(entity)
                    break
            else:
                ans.append(text[i])
                i += 1

        return "".join(ans)
