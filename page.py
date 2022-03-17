from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

BOOKING_NUMBER = "630349467"
EMAIL = "fredrik.thimgren@gmail.com"
PAGE_URL = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(PAGE_URL)

driver.find_element(By.ID, "BookingNumber").send_keys(BOOKING_NUMBER)
driver.find_element(By.ID, "ContactInfo").send_keys(EMAIL)

driver.find_element(By.NAME, "NextButtonID6").click()
driver.find_element(By.NAME, "NextButtonID26").click()
driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

driver.find_elements(by=By.XPATH, value='//*[@id="Main"]/form[2]/div[2]/table/tbody/tr/td[2]/div')

time.sleep(100000)