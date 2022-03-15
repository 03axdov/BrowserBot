from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BOOKING_NUMBER = "123131"    # Bokningsnummer
EMAIL = "a@g.com"  # Email

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://bokapass.nemoq.se/Booking/Booking/Index/stockholm')

driver.find_element(By.ID, "BookingNumber").send_keys(BOOKING_NUMBER)
driver.find_element(By.ID, "ContactInfo").send_keys(EMAIL)

driver.find_element(By.NAME, "NextButtonID6").click()