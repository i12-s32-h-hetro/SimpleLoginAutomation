from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu") 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://demo.applitools.com/index.html")
    driver.implicitly_wait(5)
except:
    print("Web page not loaded")
    driver.quit()

try:
    username = driver.find_element(By.ID, value="username").send_keys("testuser")
    password = driver.find_element(By.ID,value="password").send_keys("test123")
    signin_btn = driver.find_element(By.CSS_SELECTOR,value="#log-in").click()

except:
    print("login successfull")
    driver.quit()

