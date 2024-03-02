from requests_html import HTMLSession
from googlesearch import search
import re 

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def get_first_google_result(query):
    try:
        # Using generator to get only the first result
        search_results = search(query, num=1, stop=1, pause=2)
        return next(search_results)
    except StopIteration:
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None


def main():
    session = HTMLSession()
    query = input("query: ")
    googleResult = get_first_google_result(query)
    if googleResult is None:
        print("failed to search on google")
        return
    print("found: " + googleResult)
    response = session.get(googleResult)
    response.html.render()

    website_html = str(response.html.raw_html)
    emails = find_emails(website_html)
    print(emails)

if __name__ == "__main__":
    main()