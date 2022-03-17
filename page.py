from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

BOOKING_NUMBER = "630349467"
EMAIL = "fredrik.thimgren@gmail.com"
PAGE_URL = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"

months = {"apr": 31, "maj": 32, "jun": 31, "jul": 2}

dates = []
for key in months.keys():
    for i in range(1, months[key]):
        dates.append(f"{i} {key}")

current = dates.index("1 jul")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(PAGE_URL)

driver.find_element(By.ID, "BookingNumber").send_keys(BOOKING_NUMBER)
driver.find_element(By.ID, "ContactInfo").send_keys(EMAIL)

driver.find_element(By.NAME, "NextButtonID6").click()
driver.find_element(By.NAME, "NextButtonID26").click()
driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

while True:
    row = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/thead/tr/th')
    day = row[1].text
    if day[5:] not in dates:
        driver.refresh()
        continue
    elif dates.index(day[5:]) < current:
        elements = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/tbody/tr/td')
        for day in elements[1:]:
            print(day.text)

time.sleep(100000)

