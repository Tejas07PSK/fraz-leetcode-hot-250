class Codec:
    def __init__ (self):
        self.counter = 1
        self.base_url = "http://tinyurl.com/{}"
        self.hm = {}

    def encode (self, longUrl: str) -> str:
        key = self.base_url.format(str(self.counter))
        self.hm[key] = longUrl
        self.counter += 1
        return key

    def decode (self, shortUrl: str) -> str:
        return self.hm[shortUrl]
