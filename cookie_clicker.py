import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url="https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")

# cursor = drive.find_element(By.CSS_SELECTOR, value="#store div b")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]


timeout=time.time()+5

while True:
    cookie.click()

    if time.time()>timeout:
        all_prices=driver.find_elements(By.CSS_SELECTOR,value="#store b")
        prices=[]
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)

        menu_dict={}
        for n in range(len(prices)):
            menu_dict[item_ids[n]]=prices[n]

        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element=money_element.replace(",","")
        money=int(money_element)

        affordable_menu={}
        for item,cost in menu_dict.items():
            if money>cost:
                affordable_menu[cost]=item

        highest_prize_affordable_upgrade=max(affordable_menu)
        print(max(affordable_menu))
        print(highest_prize_affordable_upgrade)
        to_purchase=affordable_menu[highest_prize_affordable_upgrade]
        print(to_purchase)
        driver.find_element(By.ID,value=to_purchase).click()

        timeout=time.time()+5
