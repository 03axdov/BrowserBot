from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

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

def login():
    driver.find_element(By.ID, "BookingNumber").send_keys(BOOKING_NUMBER)
    driver.find_element(By.ID, "ContactInfo").send_keys(EMAIL)

    driver.find_element(By.NAME, "NextButtonID6").click()
    driver.find_element(By.NAME, "NextButtonID26").click()
    driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

login()

while True:
    try:
        row = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/thead/tr/th')
        date = row[1].text
        if date[5:] not in dates:
            driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()
            continue
        elif dates.index(date[5:]) < current:
            elements = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/tbody/tr/td/div/div')
            for day in elements[1:]:
                if day.text != "Bokad":
                    day.click()
                    break

            current = date[5:]
            driver.find_element(By.NAME, "Next").click()

    except:
        try:
            login()
        except:
            time.sleep(70)
            driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()


time.sleep(100000)

