import time
from selenium.webdriver.common.by import By


def open_url(driver, url):
    driver.get(url)
    driver.maximize_window()


def login(driver, username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()


def search(driver, url, username, password, s_key):
    open_url(driver, url)
    login(driver, username, password)
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='零售出库']").click()
    iframe_id = driver.find_element(By.XPATH, "//div[@id='tabpanel']//li[2]").get_attribute("id") + '-frame'
    driver.switch_to.frame(iframe_id)
    driver.find_element(By.ID, "searchNumber").send_keys(s_key)
    driver.find_element(By.XPATH, "//span[text()='查询']").click()
    time.sleep(2)
    num = driver.find_element(By.XPATH, "//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
