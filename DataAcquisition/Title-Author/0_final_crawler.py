from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def search_filter(year1:str, year2:str):
    fild1 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[2]/div/input")
    fild1.send_keys("Licenciatura")

    fild2 = Select(driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[3]/div/select"))
    fild2.select_by_visible_text("Grado")

    fild3 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[5]/div[1]/input[2]")
    fild3.send_keys(year1)

    fild4 = driver.find_element(by=By.XPATH, value="/html/body/section[3]/div/form/div[5]/div[2]/input[2]")
    fild4.send_keys(year2)
    
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

years = [(str(year), str(year)) for year in range(1920, 2025)]
years.insert(0, (str(1900), str(1919)))
years.insert(0, (str(1800), str(1899)))

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

for year1, year2 in years:
    if year1 == year2: title = year1 + ".txt"
    else: title = year1 + "-" + year2 + ".txt"

    try: 
        archive = open(title, "r", encoding="utf-8")
        lines = len(archive.readlines())
        archive.close()
    except: lines = 0

    link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    search_filter(year1, year2)
    n = get_number_of_thesis()
    driver.quit()

    if n == lines: continue
    else: 
        archive = open(title, "w", encoding="utf-8")
        archive.close()
        lines = 0

    while lines < n:
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        
        search_filter(year1, year2)    
        go_to_an_specific_thesis(lines)

        archive = open(title, "a", encoding="utf-8")

        start_scraping()
        bibliographic_format()
        
        for _ in range(1000):
            archive.write(extraction() + "\n")
            try: next_thesis()
            except: break
        
        archive.close()

        archive = open(title, "r", encoding="utf-8")
        lines = len(archive.readlines())
        archive.close()

        driver.quit()