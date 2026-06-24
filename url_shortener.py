import random
import string

urls = {}

def shorten(long_url):
    characters = string.ascii_letters + string.digits

    short_code = ''.join(random.choices(characters, k=6))

    while short_code in urls:
        short_code = ''.join(random.choices(characters, k=6))

    urls[short_code] = long_url

    return short_code

url = input("Enter URL: ")

code = shorten(url)

print("Short URL Code:", code)
print("Stored URLs:", urls)