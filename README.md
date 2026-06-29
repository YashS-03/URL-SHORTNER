## URL-SHORTNER
This is a simple Python project that generates a short code for a long URL.
## About the Project
The program creates a random 6-character code using letters and numbers. It checks whether the code already exists and generates a new one if needed. The short code and original URL are stored in a dictionary.
Work in progress. Currently Phase 4 - Flask Web Server
Added Flask routes:
- POST /shorten — accepts a long URL, returns a short code
- GET /<short_code> — redirects to the original URL
Fixed url_shortner.py import issue with __main__ gaurd
Implemented Flask API endpoints for URL shortening and redirection
Added SQLite-based storage with click tracking for each shortened URL
Added click tracking to count and store the number of visits for each shortened URL.
