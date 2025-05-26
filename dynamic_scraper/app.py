from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)   # 브라우저 초기화, headless는 기본적으로 True

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# page.goto("https://www.wanted.co.kr/")

# time.sleep(3)

# page.click("button.Aside_searchButton__Ib5Dn")

# time.sleep(3)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(3)

# page.keyboard.down("Enter")

# time.sleep(3)

# page.click("a#search_tab_position")

# time.sleep(3)

for x in range(5):
    page.keyboard.down("End")
    time.sleep(3)

content = page.content() 

time.sleep(3)

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title___kfvj").text
    company_name = job.find("span", class_="JobCard_companyName__kmtE0").text
    reward = job.find("span", class_="JobCard_reward__oCSIQ").text
    job = {
        "title":title,
        "company_name":company_name,
        "reward":reward,
        "link":link
    }
    jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))