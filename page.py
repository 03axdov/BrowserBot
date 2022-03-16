from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BOOKING_NUMBER = "123131"
EMAIL = "a@g.com"
PAGE_URL = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(PAGE_URL)

driver.find_element(By.ID, "BookingNumber").send_keys(BOOKING_NUMBER)
driver.find_element(By.ID, "ContactInfo").send_keys(EMAIL)

driver.find_element(By.NAME, "NextButtonID6").click()