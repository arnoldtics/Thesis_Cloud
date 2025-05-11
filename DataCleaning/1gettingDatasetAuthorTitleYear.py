import pandas as pd
import numpy as np

PATH = "../DataAcquisition/Title-Author/"

def clean(line:str) -> list:
    i = line.find(",")
    lastName = line[:i].strip()
    
    j = line.find("sustentante")
    name = line[i+1:j].strip().replace(",", "")
    
    i = j + 11
    title = line[i:].strip().split()
    title = " ".join(title[:-1])
    if title[-1] == "/": title = title[:-1]

    year = line[i:].strip().split()
    year = year[-1]
    clearYear = ""
    for symbol in year:
        if symbol.isnumeric(): clearYear += symbol

    return [name, lastName, title, clearYear]

def thesisDataframe(filename:str) -> pd.DataFrame:
    with open(PATH+filename, "r", encoding="utf-8") as data: lines = data.readlines()
    mat = np.array([clean(line) for line in lines])
    return pd.DataFrame(data=mat, columns=["Name", "Last Name", "Title", "Year"])

df = thesisDataframe("1800-1899.txt")
df = pd.concat([df, thesisDataframe("1900-1919.txt")])
for year in range(1920, 2025): df = pd.concat([df, thesisDataframe(str(year)+".txt")])
df.drop_duplicates(inplace=True)
df.to_csv("Name_LastName_Title_Year.csv", index=False)