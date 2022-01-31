from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlencode
import base64





driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

code = b'x = "hello world"\nprint(x)'
code = base64.b64encode(code)

params = {
    'colors': 'sunset',
    'background': 'true',
    'darkMode': 'true',
    'padding': '16',
    'title': 'hello',
    'code': code,
    'language': 'python',
}
url = f'https://ray.so/?{urlencode(params)}'
driver.get(url)

hide_elements = driver.find_elements(By.XPATH, '//*[@id="frame"]/div[@data-hide-when-exporting]')
for element in hide_elements:
    driver.execute_script("arguments[0].style.display = 'none';", element)

image = driver.find_element(By.ID, 'frame').screenshot('./ray.so.image.png')
driver.close()
