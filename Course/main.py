from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
# First 2 slides

# driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
# driver.implicitly_wait(3)  # time.sleep(3)
# my_element = driver.find_element("id", "downloadButton")
# my_element.click()
#
# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'progress-label'),  # Element filtration
#         'Complete!'  # The expected text
#     )
# )
# # new_element = driver.find_element("classes-name", "progress-label")
# # driver.find_element_by_class_name("progress-label")


# Third Slide
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    no_button = driver.find_element_by_class_name('at-cm-no-button')
    no_button.click()
except:
    print('No element with this class name. Skipping')
sum1 = driver.find_element_by_id('sum1')
sum2 = driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)  # This is equal to 15
sum2.send_keys(15)

btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()
