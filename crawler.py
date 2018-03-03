import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome("chromedriver.exe")
for i in range(0, 30):
    driver.get("http://software.naver.com/software/fontList.nhn?categoryId=I0000000")
    elem = driver.find_element_by_class_name("list_imgview")
    time.sleep(0.3)
    fonts = WebDriverWait(elem, 3).until(EC.presence_of_element_located((By.ID, "slot"+str(i))))

    fonts.click()
    time.sleep(0.3)
    download = driver.find_element_by_class_name("btn_buy")
    download.click()

    time.sleep(0.3)
    download = driver.find_element_by_class_name("btn_buy_v2")
    download.click()

    time.sleep(0.3)
    download = driver.find_element_by_id("downloadLink")
    download.click()

    time.sleep(0.3)
    download = driver.find_element_by_class_name("btn_lydown")
    download.click()

    time.sleep(0.3)
driver.quit()