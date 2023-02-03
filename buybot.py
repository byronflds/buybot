#import proper dependencies

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('./chromedriver', options=options)
driver.maximize_window()

#input url of item you want to purchase
driver.get('https://www.walmart.com/ip/Until-Dawn-Sony-PlayStation-4-711719039433/45463506');
time.sleep(3)

#add item to cart
addtocart = driver.find_element_by_class_name('button.button.spin-button.prod-ProductCTA--primary.button--primary')
addtocart.click();
time.sleep(3)

#click checkout using selenium
checkout = driver.find_element_by_class_name('button.button.ios-primary-btn-touch-fix.hide-content-max-m.checkoutBtn.button--primary')
checkout.click();
time.sleep(3)

#enter login info
email = driver.find_element_by_name('email').send_keys("byronflds@gmail.com")
password = driver.find_element_by_name('password').send_keys("########")
login = driver.find_element_by_class_name('button.button.width-full.button--primary').click();
