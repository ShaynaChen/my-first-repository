# 运行文件
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from python_class.common import search
from test_data import test_data1

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
url = test_data1.url["url"]
user = test_data1.user["username"]
pwd = test_data1.user["password"]
s_key = test_data1.s_key["s_key"]

result = search(driver, url, user, pwd, s_key)

if s_key in result:
    print("案例通过")
else:
    print("案例不通过")

time.sleep(1)
driver.quit()
