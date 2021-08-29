from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
html_elem = browser.find_element_by_tag_name('html')
retry_elem = browser.find_element_by_class_name('retry-button')
while True:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    if retry_elem.text == 'Try again':
        break
browser.close()
