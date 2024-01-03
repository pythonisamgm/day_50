
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


FB_EMAIL= "pythonisamgm@gmail.com"
FB_PASSWORD = "#s_G84)6Ja*/_N@"
driver = webdriver.Chrome(ChromeDriverManager().install())


def click_like():
    like_button = driver.find_element(By.XPATH,
                                      '//*[@id="u-1919424827"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
    like_button.click()
    time.sleep(4)


def click_nope():
    time.sleep(5)
    nope_button = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button')
    nope_button.click()
    time.sleep(4)

driver.get("https://tinder.com/")
privacy_settings = driver.find_element(By.XPATH, '//*[@id="u-1919424827"]/div/div[2]/div/div/div[1]/div[1]/button').click()
time.sleep(3)
log_in = driver.find_element(By.XPATH,'//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

time.sleep(3)
facebook = driver.find_element(By.XPATH,'//*[@id="u647161393"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()



#---------------------------------------------------------SWITCH WINDOWS/SIGN UP FB-------------------------------------------------------------

# to get all the window handles : driver.window_handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# switch to fb login window:
driver.switch_to.window(fb_login_window)
#print the driver title to verify. If successful title should be Facebook
print(driver.title)

time.sleep(3)
facebook_cookies=driver.find_element(By.XPATH,"//button[contains(string(), 'Permitir todas las cookies')]").click()


#login to facebook
time.sleep(2)
sign_up_email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(FB_EMAIL)
time.sleep(2)
sign_up_password = driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(FB_PASSWORD)

#login_button = driver.find_element(By.XPATH, "//input[contains(string(), 'Iniciar sesión')]")
login_button = driver.find_element(By.XPATH, "//input[@name='login'and @type='submit']")
login_button.click()

#switch to main window. If successful, title should print "Tinder | Match. Chat. Date."
driver.switch_to.window(base_window)
print(driver.title)

#---------------------------------------------------------TINDER POP UPS ----------------------------------------

#tinder: agree to location's preferences
location = driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div/div/div[3]/button[1]').click()

#tinder: decline notifications
time.sleep(5)
notifications = driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div/div/div[3]/button[2]').click()

time.sleep(5)
#cookies = driver.find_element(By.XPATH, '').click()


#click nope so you don't break any hearts, because as Miley says, "nothing breaks like a heart"
for n in range (101):
    click_nope()
    time.sleep(3)


