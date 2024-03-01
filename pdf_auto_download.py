from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.prompt_for_download': False,
    'plugins.always_open_pdf_externally': True
})

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


URL = "https://www.nmdpra.gov.ng/StockReport"
driver.get(URL)

# Increase the implicit wait time to ensure elements are loaded
driver.implicitly_wait(20)

# Locate the button using its class name
download_button = driver.find_element(By.CLASS_NAME, "btn-primary")

# Click on the button
download_button.click()

# Allow some time for the new page or download to load
time.sleep(5)

# Close the WebDriver at the end
driver.quit()