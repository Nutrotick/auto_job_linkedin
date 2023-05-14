from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Add chromedriver from disk
service = Service("C:\Pythonistan\files for development\chromedriver_win32\chromedriver.exe")
# Make window opened
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3536248797&f_LF=f_AL&geoId=90010216&keywords=python%20developer&location=Kyiv%20Metropolitan%20Area&refresh=true")
driver.maximize_window()

login_button = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
time.sleep(1)
login_button.click()
email_button = driver.find_element(By.CSS_SELECTOR, "#username")
email_button.send_keys("YOUR USERNAME")
password_button = driver.find_element(By.CSS_SELECTOR, "#password")
password_button.send_keys("YOUR PASSWORD")
submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()
hide_popup = driver.find_element(By.ID, "ember127")
time.sleep(1)
hide_popup.click()
save_job = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
save_job.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
follow_job = driver.find_element(By.CLASS_NAME, "follow")
# ActionChains(driver)\
#     .scroll_to_element(follow_job)\
#     .perform()
follow_job.click()