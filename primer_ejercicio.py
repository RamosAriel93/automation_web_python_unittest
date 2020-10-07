import time

from selenium import webdriver

driver = webdriver.Chrome('/home/gabriela/PycharmProjects/automation_proyect/chromedriver')

driver.get('http://automationpractice.com/index.php')
driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
time.sleep(4)
error = driver.find_element_by_xpath('//*[@id="center_column"]/p').text

assert error == 'No results were found for your search "hola"'

driver.close()
driver.quit()
