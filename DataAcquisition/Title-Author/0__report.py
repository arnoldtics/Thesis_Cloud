from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd

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

years = [(str(year), str(year)) for year in range(1920, 2026)]
years.insert(0, (str(1900), str(1919)))
years.insert(0, (str(1800), str(1899)))

link = "https://tesiunam.dgb.unam.mx/F?func=find-b-0&local_base=TES01"

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito')

df = pd.read_csv("../../DataCleaning/Author_Title_Link_Year.zip")
df["Year"] = df["Year"].astype('int')

with open("report.txt", "w") as f:
    for year1, year2 in years:

        driver = webdriver.Chrome(options=options)
        driver.get(link)
        search_filter(year1, year2)
        n = get_number_of_thesis()
        
        if year1 == year2:
            count = df[df["Year"] == int(year1)].shape[0]
            if n - count:
                f.write(f"{year1} {n - count}\n")
        else:
            count = df[(df["Year"] >= int(year1)) & (df["Year"] <= int(year2))].shape[0]
            if n - count:
                f.write(f"{year1} {year2} {n - count}\n")

        print(year1, n-count)
        # driver.quit()