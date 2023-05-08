from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '/Users/gbcrockett/Desktop/python/chromedriver'
tweet_count = 0
driver = webdriver.Chrome(PATH)
# with open('prophecies.txt', 'r') as f:
#     lines = f.readlines()

driver.get('https://www.twitter.com')

time.sleep(3)

log_in = driver.find_element(By.XPATH, '//a[@href="/login"]')
print(log_in.text)
log_in.click()
time.sleep(3)
input = driver.find_element(By.TAG_NAME, 'input')
input.send_keys('jeffcrockettreddit@gmail.com')
input.send_keys(Keys.RETURN)
time.sleep(3)
inputs = driver.find_elements(By.TAG_NAME, 'input')
username = inputs[-1]
username.send_keys('leovinus42')
username.send_keys(Keys.RETURN)
time.sleep(3)
inputs = driver.find_elements(By.TAG_NAME, 'input')
password = inputs[-1]
password.send_keys('Jcr=38251013')
password.send_keys(Keys.RETURN)
time.sleep(3)

#go to trending
# explore = driver.find_element(By.XPATH, '//a[@href="/explore"]')
# explore.click()
# time.sleep(3)
# trending = driver.find_element(By.XPATH, '//a[@href="/explore/tabs/trending"]')
# trending.click()
# time.sleep(3)
# trending_links = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
# print('number of trending links', len(trending_links))
for i in range(10, -1, -1): 
    # driver.get('https://twitter.com/explore/tabs/sports_unified')
    driver.get('https://twitter.com/explore/tabs/entertainment_unified')
    # driver.get('https://twitter.com/explore/tabs/news_unified')
    # driver.get('https://twitter.com/explore/tabs/trending')
    # time.sleep(5)
    trending_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="trend"]')))
    # trending_links = driver.find_elements(By.XPATH, '//div[@data-testid="trend"]')
    if i >= len(trending_links):
        continue
    link = trending_links[i]
    # time.sleep(5)
    link.click()    
    # time.sleep(5)
    # tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')

    for i in range(10):
        # tweets = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-testid="tweetText"]')))
        time.sleep(5)
        tweets = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')

        print(len(tweets))
        if i < len(tweets):
            tweets[i].click()
        else:
            break
        # time.sleep(5)
        reply_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'public-DraftStyleDefault-block')))
        # reply_box = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        reply_box.send_keys('wow, what a great tweet! please tell me more!')
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        send_button.click()
        tweet_count += 1
        print(f'{tweet_count} tweets sent')
        time.sleep(3)
        driver.back()
time.sleep(10)

#send tweet
# text_box = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
# text_box.send_keys("i'm not a bot! beep boop!")
# tweet = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
# tweet.click()


# time.sleep(10)