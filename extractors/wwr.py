from bs4 import BeautifulSoup
import cloudscraper

def extract_wwr_jobs(keyword):
    scraper = cloudscraper.create_scraper()
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = scraper.get(f"{base_url}{keyword}")
    print("response.status_code=",response.status_code)
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company = post.find("p", class_="new-listing__company-name").text
                region = post.find("p", class_="new-listing__company-headquarters").text
                title = post.find('h4', class_='new-listing__header__title').text
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.replace(",", " "),
                    'location': region.replace(",", " "),
                    'position': title.replace(",", " ")
                }
                results.append(job_data)
        return results