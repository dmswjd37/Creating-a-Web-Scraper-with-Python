import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper() # returns a requests.Session object

all_jobs = []

def scrape_page(url):
    print(f"Scrapping {url}...")
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

    for job in jobs:
        title = job.find("h4", class_="new-listing__header__title").text
        region_tag = job.find("p", class_="new-listing__company-headquarters")
        region = region_tag.get_text if region_tag else "N/A"
        company = job.find("p", class_="new-listing__company-name").text
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        
        job_data = {
            "title": title,
            "region": region,
            "company": company,
            "url": f"https://weworkremotely.com/{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))