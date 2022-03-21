from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gc

while True:
    print("Started program")
    BOOKING_NUMBER = "" # Your booking-number goes here
    EMAIL = ""  # Your email goes here
    PAGE_URL = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"
    ITER = 0

    months = {"mar": 32, "apr": 31, "maj": 32, "jun": 31, "jul": 32, "aug": 31, "sep": 31}

    dates = []
    for key in months.keys():
        for i in range(1, months[key]):
            dates.append(f"{i} {key}")

    current = dates.index("")   # Add the date of your current time withing the quotes. Ex. 21 jan or 3 mar

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
                print("Better time")
                print(date[4:])
                elements = driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/tbody/tr/td/div/div')
                for day in elements:
                    if day.text != "Bokad":
                        day.click()
                        break

                current = dates.index(date[4:])
                driver.find_element(By.NAME, "Next").click()
                driver.find_element(By.NAME, "Next").click()
                print("Clicked next 2 times")
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                driver.switch_to.alert.accept()
                print("Accepted notification")
                driver.find_element(By.NAME, "NextButtonID6").click()
                driver.find_element(By.NAME, "NextButtonID26").click()
                driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()
                print(f"Booked time: {date[4:]}")
            elif dates.index(date[4:]) == current:
                time.sleep(5)
                driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

        except:
            try:
                login()
            except:
                ITER += 1
                if ITER == 50:
                    print("ITER == 50")
                    gc.collect()
                    break
                time.sleep(63)
                try:
                    driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()
                except:
                    driver.get(PAGE_URL)
                    login()
