from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--disable-gpu')  # Disable GPU usage

# Specify the ChromeDriver service with the path to the executable
service = Service(executable_path=ChromeDriverManager().install())

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the TikTok search URL
driver.get("https://www.tiktok.com/search?q=podcast")
print(driver.page_source)
# Wait for the page to load and then find the div elements with the partial class name
# divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class*="DivItemContainerForSearch"]')))
# print(driver.find_element(By.CSS_SELECTOR, "div[class^='DivItemContainerForSearch']"))
# Iterate over the divs and find the anchor elements with href attributes
# for div in divs:
#     links = div.find_elements(By.CSS_SELECTOR, 'a[href]')
#     for link in links:
#         print(link.get_attribute('href'))

# Quit the driver when done
driver.quit()
