import cloudscraper
from bs4 import BeautifulSoup

class RemoteOkScraper:
    BASE_URL = "https://remoteok.com"

    def __init__(self):
        self.scraper = cloudscraper.create_scraper()

    def build_url(self, keyword):
        return f"{self.BASE_URL}/remote-{keyword}-jobs"

    def scrape_page(self, keyword):
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"Scrapping {url}...")

        print("--Job Scraping Starts--")
        jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")[0:]

        for job in jobs:
            title = job.find("h2", itemprop="title").text
            company = job.find("h3", itemprop="name").text

            region = scraper.get_region(job)   # 이모지 제거 후 국가 이름만 추출

            url = job.find("td", class_="image").find("a", class_="preventLink")
            print(region)

    def get_region(self, job):
        region_text = job.find("div", class_="location").text.split(maxsplit=1)
        return region_text[1] if len(region_text) > 1 else region_text[0]

if __name__ == "__main__":
    keywords = ["flutter"]
    print("Keywords list:", keywords)

    scraper = RemoteOkScraper()

    for keyword in keywords:
        url = scraper.build_url(keyword)
        scraper.scrape_page(url)