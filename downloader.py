from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os

food = input("Enter keyword: ")
img_path = "./images/{}".format(food)
num = int(input("How many? "))

if not os.path.isdir(img_path):
    os.mkdir(img_path)

driver = webdriver.Chrome("./chromedriver.exe")
driver.get('https://www.google.com/')

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
box.send_keys(food)
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[4]/div[2]/input').click()
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, num+1):
    try:
        img_name = img_path + "/{}_{}.png".format(food, i)
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(i)).screenshot(img_name)
    except Exception as e:
        print(e)