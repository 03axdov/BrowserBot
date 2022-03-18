from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BOOKING_NUMBER = ""
EMAIL = ""
PAGE_URL = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"

months = {"mar": 32,"apr": 31, "maj": 32, "jun": 31, "jul": 32, "aug": 31}

dates = []
for key in months.keys():
    for i in range(1, months[key]):
        dates.append(f"{i} {key}")

current = dates.index("")

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
        if date[4:] not in dates or dates.index(date[4:]) > current:
            time.sleep(5)
            driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()
        elif dates.index(date[4:]) < current:
            elements = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/tbody/tr/td/div/div')
            for day in elements:
                if day.text != "Bokad":
                    day.click()
                    break

            current = dates.index(date[4:])
            driver.find_element(By.NAME, "Next").click()
            driver.find_element(By.NAME, "Next").click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            driver.find_element(By.NAME, "NextButtonID6").click()
            driver.find_element(By.NAME, "NextButtonID26").click()
            driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

    except:
        try:
            login()
        except:
            time.sleep(63)
            try:
                driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()
            except:
                driver.get(PAGE_URL)
                login()
