import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

ser = Service(r"D:\Developers Institute\DevelopersInstitute\Week7\Hackathon\chromedriver.exe")

driver = webdriver.Chrome(service=ser,options=options)
driver.get("https://postal-codes.cybo.com/india/400101/")
time.sleep(2)

# a = driver.find_elements_by_xpath("//table[@class='nw-table']//tr[3]//td[1]")
a=driver.find_element(By.XPATH, "//table[@class='nw-table']//tr[3]//td[1]")
print("malhar",a)
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='pixlee_lightbox_iframe']")))
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='vote_button mfp-voteText']"))).click()
# b=driver.find_element(By.CSS_SELECTOR, "#content > div.postal-flex > div.p-content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)").text
# print("css",b)
# b=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]")
# print("web",b)
driver.close()