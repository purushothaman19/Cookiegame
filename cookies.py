from selenium import webdriver
from datetime import datetime

chrome_driver_path = 'chromedriver--path'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

cookie_url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(cookie_url)

cookie = driver.find_element_by_id('cookie')

boost_ups = ["buyTime machine",
             "buyPortal",
             "buyAlchemy lab",
             "buyShipment",
             "buyMine",
             "buyFactory",
             "buyGrandma",
             "buyCursor"]

boost_cost = [up.text.split().pop().replace(',', '') for up in driver.find_elements_by_css_selector('.grayed b') if up.
              text != '']

boost_cost.reverse()

stop_time = datetime.now().minute + 5

if datetime.now().second < 55:
    check_sec = datetime.now().second + 5
else:
    check_sec = datetime.now().second - 55

while datetime.now().minute != stop_time:

    if check_sec == datetime.now().second:

        money = driver.find_element_by_id('money')
        int_money = int(money.text)
        print(check_sec, 'c')
        print(datetime.now().second, 's')

        for i in range(len(boost_cost)):
            int_boost_cost = int(boost_cost[i])

            if int_boost_cost < int_money:
                boost_click = driver.find_element_by_id(boost_ups[i])
                boost_click.click()
                break

        if datetime.now().second < 55:
            check_sec = datetime.now().second + 5
        else:
            check_sec = datetime.now().second - 55

    else:
        cookie.click()

click_rate = driver.find_element_by_id('cps')
print(click_rate)
