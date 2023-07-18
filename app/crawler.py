import requests
from bs4 import BeautifulSoup

# Your login details
payload = {
    'emailAddress': 'chakhan.lk9@gmail.com',  # replace with your email
    'password': 'VYP7&v9Wh5#J'  # replace with your password
}

# Use 'with' to ensure the session context is closed after use
with requests.Session() as s:
    url = 'https://cardano.ideascale.com/a/community/login'  # replace with the website you're logging into
    response = s.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the CSRF token if the website uses one
    # This is just an example. The actual token name can be different
    # and needs to be inspected from the webpage source.
    # csrf = soup.find('input', attrs={'name': 'csrf_token'})['value']
    # payload['csrf_token'] = csrf

    post = s.post(url, data=payload)
    print(post.text)  # the HTML content of the page after login
