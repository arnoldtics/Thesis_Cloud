from time import sleep
from datetime import datetime
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def search_filter(year:str):
    fild1 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[2]/div/input")
    fild1.send_keys("Licenciatura")

    fild2 = Select(driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[3]/div/select"))
    fild2.select_by_visible_text("Grado")

    fild3 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[5]/div[1]/input[2]")
    fild3.send_keys(year)

    fild4 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[5]/div[2]/input[2]")
    fild4.send_keys(year)
    
    do_search = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[6]/div/button")
    do_search.click()

def get_number_of_thesis() -> int:
    text1 = driver.find_element(by=By.XPATH, value="/html/body/section[5]/div/div/div/p/strong").text.strip().split()
    return int(text1[-1][:-1])

def start_scraping():
    first_thesis = driver.find_element(by=By.XPATH, value="/html/body/section[7]/div/div/div/div/table/tbody[1]/tr/td[4]/a")
    first_thesis.click()

def bibliographic_format():
    button = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/div/div/ul/li[4]/a")
    button.click()

def extraction():
    data = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody[2]/tr/td").text
    return data

def next_thesis():
    button = driver.find_element(by=By.XPATH, value="//img[@title='Registro siguiente']")
    button.click()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

year = str(datetime.now())[:4]

link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"
driver = webdriver.Chrome(options=options)
driver.get(link)
sleep(1)

search_filter(year)
sleep(1)

n = get_number_of_thesis()
try: 
    archive = open(year + ".txt", "r", encoding="utf-8")
    lines = archive.readlines()
except: 
    archive = open(year + ".txt", "x", encoding="utf-8")
    lines = []

if len(lines) != n: 
    archive.close()
    archive = open(year + ".txt", "a", encoding="utf-8")
    n -= len(lines)
    start_scraping()
    sleep(1)
    bibliographic_format()
    thesis = []
    for _ in range(n):
        sleep(r.uniform(0.35, 0.75))
        thesis.append(extraction())
        try: next_thesis()
        except: break
    for t in reversed(thesis): archive.write(t + "\n")

archive.close()
driver.quit()