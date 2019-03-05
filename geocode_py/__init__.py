from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from geocode import geocode

def main():
	url = "http://www.map.com.tw/"
	headers = {'Referer': url,
	           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
	print('hi')
	# 使用chrome驅動器
	browser = webdriver.Chrome()

	# 每一個網頁不超過10秒
	browser.set_page_load_timeout(10)
	browser.get(url)
	print(geocode(browser,addr))



if __name__ == '__main__':
    main()