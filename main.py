from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


FB_EMAIL= FB_EMAIL
FB_PASSWORD = FB_PASSWORD
driver = webdriver.Chrome(ChromeDriverManager().install())


def click_like():
    for n in range(30):
        try:
            driver.find_element(By.TAG_NAME,
                                              "body").send_keys(Keys.ARROW_RIGHT)
            time.sleep(4)
        except ElementClickInterceptedException:
            try:
                driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                time.sleep(2)
            except NoSuchElementException:
                time.sleep(3)

def click_nope():
    for n in range(30):
        driver.find_element(By.TAG_NAME,
                            "body").send_keys(Keys.ARROW_LEFT)
        time.sleep(5)
        try:
            #add tinder shortcut decline.
            driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div[2]/button[2]').click()
            print("we got so far")
            time.sleep(10)
            # tinder gold decline.
            driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div[2]/button').click()
        except NoSuchElementException:
            print("nope")



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
time.sleep(15)
#tinder: agree to location's preferences
location = driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div/div/div[3]/button[1]').click()

#tinder: decline notifications
time.sleep(5)
notifications = driver.find_element(By.XPATH, '//*[@id="u647161393"]/main/div/div/div/div[3]/button[2]').click()

time.sleep(5)
#cookies = driver.find_element(By.XPATH, '').click()


# Uncoment the function you prefer: click_like or click_nope so you don't break any hearts, because as Miley says, "nothing breaks like a heart"

#click_like()
click_nope()



