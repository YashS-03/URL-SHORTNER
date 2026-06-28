import random
import string
from database import save_url,get_url

def shorten(long_url):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(characters, k=6))

    while get_url(short_code):
        short_code = ''.join(random.choices(characters, k=6))

    save_url(long_url, short_code)
    return short_code

if __name__ == "__main__":
    url = input("Enter URL : ")
    code = shorten(url)
    print("Short URL Code")