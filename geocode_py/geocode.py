from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# addr = '桃園市中壢區中北路二段460號'



def geocode(browser,addr):
    url_map = "http://www.map.com.tw/"
    browser.get(url_map)
    browser.find_element_by_css_selector('#searchWord').clear()
    browser.find_element_by_css_selector('#searchWord').send_keys(addr)
    browser.find_element_by_css_selector('#Menu > div.search > img:nth-child(3)').click()
    browser.implicitly_wait(10)
    lng = browser.find_element_by_css_selector('#customMarkinfowindow > div > .winfoIframe').get_attribute('src').split('x=')[1].split('&')[0]
    lat = browser.find_element_by_css_selector('#customMarkinfowindow > div > .winfoIframe').get_attribute('src').split('y=')[1].split('&')[0]
    browser.refresh()
    return (lng,lat)
