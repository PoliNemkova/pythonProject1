import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

driver = webdriver.Chrome()

# driver = webdriver.Chrome()
#driver.get("https://www.revolve.com/dresses/br/a8e981/?navsrc=main")
driver.get("https://www.revolve.com/jackets-coats/br/e4012a/?navsrc=subclothing")
results = []
time.sleep(3)
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

# Picking a name that represents the function will be useful as you expand your code.
def parse_image_urls(cssSelector, location, source):
    for a in soup.select(cssSelector):
        name = a.get("id")
        results.append(f"https://is4.revolveassets.com/images/p4/n/z/{name}_V1.jpg")
        results.append(f"https://is4.revolveassets.com/images/p4/n/z/{name}_V2.jpg")
        results.append(f"https://is4.revolveassets.com/images/p4/n/z/{name}_V3.jpg")
        results.append(f"https://is4.revolveassets.com/images/p4/n/z/{name}_V4.jpg")
    return results

parse_image_urls('li[class*="js-plp-container"]', "img", "src")

df = pd.DataFrame({"links": results})
df.to_csv("links.csv", index=False, encoding="utf-8")
