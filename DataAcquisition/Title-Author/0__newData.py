from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd

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

df = pd.read_csv("../../DataCleaning/Author_Title_Link_Year.zip")
df["Year"] = df["Year"].astype('int')

year = ""

link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"
driver = webdriver.Chrome(options=options)
driver.get(link)

with open(year + ".txt", "r", encoding="utf8") as f:
    lines = f.readlines()

search_filter(year)
n = get_number_of_thesis()
start_scraping()
bibliographic_format()

with open(year + ".txt", "a", encoding="utf8") as f:
    for _ in range(n):
        data = extraction() + "\n"
        if not (data in lines):
            print(data)
            f.write(data)
        try: next_thesis()
        except: break

driver.quit()