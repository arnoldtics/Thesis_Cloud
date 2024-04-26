import pandas as pd
import numpy as np

PATH = "../DataAcquisition/Title-Author/"

def clean(line:str) -> list:
    i = line.find(",")
    lastName = line[:i].strip()

    j = line.find("sustentante")
    name = line[i+1:j].strip().replace(",", "")
    
    i = j + 11
    title = line[i:-9].strip()
    
    year = line[-9:].strip()
    clearYear = ""
    for symbol in year:
        if symbol.isnumeric(): clearYear += symbol
    if len(clearYear) > 4: clearYear = clearYear[1:]
    
    fullname = name.strip() + " " + lastName.strip()
    
    return [fullname, title, clearYear]

def thesisDataframe(filename:str) -> pd.DataFrame:
    with open(PATH+filename, "r", encoding="utf-8") as data: 
        mat, lines = [], data.readlines()
        for line in lines:
            if line.startswith("https://tesiunam.dgb.unam.mx"):
                line = line.strip().replace("\"", "").replace("\n", "")
                instance.insert(2, line)
                mat.append(instance)
            else: instance = clean(line)
        mat = np.array(mat)
    return pd.DataFrame(data=mat, columns=["Name", "Title", "Link", "Year"])

df = thesisDataframe("1800-1899_thesis-link.txt")
df = pd.concat([df, thesisDataframe("1900-1919_thesis-link.txt")])
for year in range(1920, 2025): df = pd.concat([df, thesisDataframe(str(year)+"_thesis-link.txt")])
df.to_csv("Author_Title_Link_Year.csv", index=False)