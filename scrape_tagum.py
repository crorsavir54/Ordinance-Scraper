import requests
import csv
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filename = "tagum_ordinances.csv"

csv_writer = csv.writer(open(filename, 'w'))

options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://sp.tagumcity.gov.ph/category/ordinances/page/1")

def scrape():
	for wrapper in soup.find_all("div", {"class": "post-box"}):
		data = []
		for title in wrapper.find_all("h2", {"class": "entry-title"}):
			data.append(title.text.strip())
			for content in wrapper.find_all("div", {"class": "entry-content"}):
				data.append(content.text.strip())
		if data:
			print("Inserting data: {}".format(','.join(data)))
			csv_writer.writerow(data)
# scrape current page first
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html")
scrape()

#scrape next pages
n = 1

while n<134:
	try:
		n = n + 1
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//nav[@id='nav-below']/div/a"))).click()
		page_source = driver.page_source
		soup = BeautifulSoup(page_source, "html")
		scrape()
		print("Next page clicked")
		print(n)    
	except TimeoutException:
		print("No more pages")
		break
driver.quit()