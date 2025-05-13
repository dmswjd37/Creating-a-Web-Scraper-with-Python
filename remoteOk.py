import cloudscraper
from bs4 import BeautifulSoup

class remoteOk:

    
    scraper = cloudscraper.create_scraper() # returns a requests.Session object
    response = scraper.get("https://remoteok.com/remote-flutter-jobs")
    soup = BeautifulSoup(response.text, "html.parser")

if __name__ == "__main__":
    keywords = ["flutter", "python", "golang"]

    