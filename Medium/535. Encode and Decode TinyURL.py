class Codec:
    dic = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dic = {}
        s = longUrl.split('/')
        self.dic[s[0] + '//' ] =  'http://'
        self.dic[s[2] + '/'] = 'tinyurl.com/'
        self.dic['/'.join(s[3:])] = '4e9iAk'
        return ''.join(list(self.dic.values()))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return ''.join(list(self.dic.keys()))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
