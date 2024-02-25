from time import sleep
import random as r
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def search_filter(input:int, field:int):
    fild1 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[2]/div/input")
    fild1.send_keys(input)

    fild2 = Select(driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[3]/div/select"))
    fild2.select_by_visible_text(field)
    
    do_search = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[6]/div/button")
    do_search.click()

def refine_search(input:int, field:int):
    button = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/div/div/ul/li[2]/a")
    button.click()
    sleep(2)
    
    fild1 = driver.find_element(by=By.XPATH, value="/html/body/section[4]/div/form/div[2]/div/input")
    fild1.send_keys(input)
    
    fild2 = Select(driver.find_element(by=By.XPATH, value="/html/body/section[4]/div/form/div[3]/div/select"))
    fild2.select_by_visible_text(field)

    do_search = driver.find_element(by=By.XPATH, value="/html/body/section[4]/div/form/div[5]/div/button")
    do_search.click()

def get_number_of_thesis() -> int:
    text1 = driver.find_element(by=By.XPATH, value="/html/body/section[5]/div/div/div/p/strong").text.strip().split()
    return int(text1[-1][:-1])

def start_scraping():
    first_thesis = driver.find_element(by=By.XPATH, value="/html/body/section[7]/div/div/div/div/table/tbody[1]/tr/td[4]/a")
    first_thesis.click()

def extraction():
    program = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[9]/td/a").text
    year = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[3]/td").text
    title = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div/div/table/tbody/tr[2]/td").text
    return (program, year, title)

def next_thesis():
    button = driver.find_element(by=By.XPATH, value="//img[@title='Registro siguiente']")
    button.click()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"
driver = webdriver.Chrome(options=options)
driver.get(link)
sleep(2)

search_filter("Licenciatura", "Grado")
sleep(2)
refine_search("Escuela Nacional de Estudios Superiores Morelia", "Escuela/Facultad")
sleep(2)

current_number_of_thesis = get_number_of_thesis()
data = open("thesis3.txt", "r", encoding="utf-8")
last_number_of_thesis = len(data.readlines())
if current_number_of_thesis - last_number_of_thesis == 0:
    data.close()
    driver.quit()
else:
    number_of_thesis = current_number_of_thesis - last_number_of_thesis

    start_scraping()
    sleep(2)

    thesis = []
    for _ in range(number_of_thesis):
        thesis.append(extraction())
        sleep(r.uniform(0.5, 1))
        try: next_thesis()
        except: break

    data = open("thesis1.txt", "a", encoding="utf-8")
    for program, year, title in reversed(thesis): data.write(f"{program}. {year}. {title}\n")
    data.close()
    driver.quit()