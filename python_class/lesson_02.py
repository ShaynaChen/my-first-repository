import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
# 基本操作
# 1、打开网页
# driver.get("https://www.google.com")
# # 2、窗口最大化
# driver.maximize_window()
# # 3、等待3秒后再打开一个网页
# time.sleep(2)
# driver.get("https://www.baidu.com")
# # 4、后退，前进，刷新页面
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# # 5、退出网页
# # driver.quit()  # 关闭浏览器
# driver.close()  # 关闭网页

driver.get("http://erp.lemfix.com/login.html")
driver.implicitly_wait(10)
driver.find_element(By.ID, "username").send_keys("test123")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "btnSubmit").click()

# text1 = driver.find_element(By.XPATH, "//div[@class='login-logo']//b").text
# print(text1)

driver.find_element(By.XPATH, "//span[text()='零售出库']").click()

# iframe_id = driver.find_element(By.XPATH, "//div[@id='tabpanel']//li[2]").get_attribute("id") + '-frame'
# driver.switch_to.frame(iframe_id)

driver.switch_to.frame(1)
driver.find_element(By.ID, "searchNumber").send_keys("9256")
driver.find_element(By.XPATH, "//span[text()='查询']").click()
time.sleep(2)
num = driver.find_element(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
# print(num)

if "9526" in num:
    print("案例通过")
else:
    print("案例不通过")

time.sleep(1)
driver.quit()

