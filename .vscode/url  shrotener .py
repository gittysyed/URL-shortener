import hashlib

class URLshortener:
    def __init__(self):
        self.urls = {}
      
    def shorten_url(self, long_url):
        hash_object = hashlib.md5(long_url.encode())
        short_code = hash_object.hexdigest()[:6]

        # Store the short code with the original URL
        self.urls[short_code] = long_url

        return f"https://your- urlexampleshort-domain/{short_code}"
    
    def get_original_url(self, short_code):
        # Retrieve the original URL from the dictionary which we have stored
        return self.urls.get(short_code, None)

# For example usage:
if __name__ == "__main__":
    shortener = URLshortener()
    original_url = "https://www.urlexample.com/very-long-url-that-needs-to-be-shortened"

    short_url = shortener.shorten_url(original_url)
    print(f"Shortened URL: {short_url}")

    retrieved_url = shortener.get_original_url(short_url.split('/')[-1])
    print(f"Original URL: {retrieved_url}")
