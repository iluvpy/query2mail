from requests_html import HTMLSession
import re 

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

session = HTMLSession()
url = input("URL: ")
response = session.get(url)
response.html.render()

website_html = str(response.html.raw_html)
emails = find_emails(website_html)
print(emails)