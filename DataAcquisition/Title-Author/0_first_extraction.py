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

def go_to_an_specific_thesis(n:int):
    n = str(n+1)
    field = driver.find_element(by=By.XPATH, value="/html/body/section[6]/div/div/div[1]/form/input[2]")
    field.send_keys(n)
    field.send_keys(Keys.RETURN)

def binary(arr, x):
    n = len(arr)
    if n == 0: return -1
    a, b = 0, n - 1
    while a <= b:
        m = (a+b)//2
        if arr[m] == x: return m
        elif arr[m] < x: a = m + 1
        else: b = m - 1
    return -1

year = input("Write the year:\n").strip()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

try: 
    archive = open(year + ".txt", "r", encoding="utf-8")
    previous = sorted(archive.readlines())
    archive.close()
except: previous = []

link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"
driver = webdriver.Chrome(options=options)
driver.get(link)
search_filter(year)
n, lines = get_number_of_thesis(), 0
driver.quit()

while lines < n:
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    
    search_filter(year)    
    go_to_an_specific_thesis(lines)

    archive = open(year + ".txt", "a", encoding="utf-8")

    start_scraping()
    bibliographic_format()
    
    for _ in range(1000):
        data = extraction() + "\n" 
        i = binary(previous, data)
        if i == -1: archive.write(data)
        try: next_thesis()
        except: break
    
    archive.close()

    archive = open(year + ".txt", "r", encoding="utf-8")
    lines = len(archive.readlines())
    archive.close()

    driver.quit()