import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper() # returns a requests.Session object

all_jobs = []

def scrape_page(url):
    response = scraper.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find("section", id="category-2").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("h4", class_="new-listing__header__title").text
        region = job.find("p", class_="new-listing__company-headquarters").text
        company = job.find("p", class_="new-listing__company-name").text
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        
        job_data = {
            "title": title,
            "region": region,
            "company": company,
            "url": f"https://weworkremotely.com/{url}"
        }
        all_jobs.append(job_data)

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

print(all_jobs)