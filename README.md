# URL-SHORTNER
This is a simple Python project that generates a short code for a long URL.
## About the Project
The program creates a random 6-character code using letters and numbers. It checks whether the code already exists and generates a new one if needed. The short code and original URL are stored in a dictionary.
## Features
- Generates a random short URL code
- Prevents duplicate codes
- Stores URL mappings using a dictionary
- Easy to understand and modify
## Technologies Used
- Python
- Random Module
- String Module
## How It Works
1. User enters a long URL.
2. Program generates a random 6-character code.
3. The code is checked for duplicates.
4. The code and URL are stored in a dictionary.
5. The short code is displayed to the user.
## Example
Input:
```
https://www.google.com
```
Output:
```
Short URL Code: A7xP2m
```
## Project Structure
```
url-shortener/
│
├── url_shortener.py
└── README.md
```
## Future Improvements
- Save URLs permanently using a database
- Create a web interface
- Allow custom short codes
- Add URL redirection
