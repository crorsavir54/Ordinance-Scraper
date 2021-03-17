import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

filename = "davao_ordinances.csv"

csv_writer = csv.writer(open(filename, 'w'))

options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://ordinances.davaocity.gov.ph/")

def scrape():
	for tr in soup.find_all('tr')[2:][:-2]:
		data = []
		for td in tr.find_all('td'):
			data.append(td.text.strip())
		if data:
			print("Inserting data: {}".format(','.join(data)))
			csv_writer.writerow(data)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html")
scrape()
n = 1
while n < 42: #42 pages in website
	n = n + 1
	driver.find_element_by_link_text(str(n)).click()
	page_source = driver.page_source
	soup = BeautifulSoup(page_source, "html")
	scrape()
driver.quit()
