import cloudscraper
from bs4 import BeautifulSoup

class Job:
    def __init__(self, title, company, region, link):
        self.title = title
        self.company = company
        self.region = region
        self.link = link

    def __str__(self):
        return f"{self.title} / {self.company} / {self.region} / {self.link}"
    
    def __repr__(self):
        return f"{self.title} / {self.company} / {self.region} / {self.link}"

class RemoteOkScraper:
    BASE_URL = "https://remoteok.com"

    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.all_jobs = []

    def build_url(self, keyword):
        '''url 생성'''
        print("✅ Create URL with job keyword...")
        return f"{self.BASE_URL}/remote-{keyword}-jobs"

    def scrape_page(self, url):
        print(f"✅ Scrapping {url}...")
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        print("✅ --Job Scraping Starts--")
        jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

        for job in jobs:
            title = job.find("h2", itemprop="title").text
            company = job.find("h3", itemprop="name").text

            region = scraper.get_region(job)   # 이모지 제거 후 국가 이름만 추출

            link_tag = job.find("td", class_="image").find("a", class_="preventLink")["href"]
            link = f"{self.BASE_URL}{link_tag}"
            
            job_list = Job(title.strip(), company.strip(), region.strip(), link.strip())    # 양쪽 공백 제거
            self.all_jobs.append(job_list)

    def get_region(self, job):
        '''이모지 제거 후 국가 이름만 추출'''
        region_text = job.find("div", class_="location").text.split(maxsplit=1)
        return region_text[1] if len(region_text) > 1 else region_text[0]

if __name__ == "__main__":
    keywords = ["flutter", "python", "golang"]
    print("✅ Keywords list:", keywords)

    scraper = RemoteOkScraper()

    for keyword in keywords:
        url = scraper.build_url(keyword)
        scraper.scrape_page(url)
        print(scraper.all_jobs)
        print("✅ --Job Scraping End--")
        scraper.all_jobs.clear  # 각각의 keyword 별로 출력되도록 list clear