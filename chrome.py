import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MNEMONIC = 'security curve swallow few tilt attract donor tuition matter place spoon major'.split(' ')
PASSWORD = '11111111'

#--------------------------------------------------selenium config
chrome_options = Options()
chrome_options.add_extension('MetaMask_Chrome.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
time.sleep(0.5)
#--------------------------------------------------

# fix "Message: unknown error: Runtime.callFunctionOn threw exception: Error: LavaMoat"  
# solution: https://github.com/LavaMoat/LavaMoat/pull/360#issuecomment-1547271080
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input').click() # agree to TOS 
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button').click() # import 
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div/button[2]').click() # no thanks
time.sleep(0.5)
for i in range(3): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # locate mnemonic box
for word in MNEMONIC:
    driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
    for i in range(2): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    # time.sleep(0.5)
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(PASSWORD) # enter password
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(PASSWORD) # enter password twice
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click() # I understand
driver.find_element('xpath', '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # import my wallet
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # got it
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # next page
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # done
time.sleep(1)
driver.find_element('xpath', '/html/body/div[2]/div/div/section/div[1]/div/button/span').click() # close

print('import complete')
time.sleep(999999)