import numpy as np
import matplotlib.pyplot as plt

PATH, frequency = "../DataAcquisition/Title-Author/", {}

def counting(filename):
    with open(PATH + filename, "r", encoding="latin1") as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith("https://tesiunam.dgb.unam.mx"):
                year, line = "", line.strip()
                for character in reversed(line):
                    if character.isnumeric(): year = character + year
                    if len(year) == 4: break
                try: frequency[int(year)] += 1
                except: frequency[int(year)] = 1

counting("1800-1899_thesis-link.txt")
counting("1900-1919_thesis-link.txt")

for year in range(1920, 2025):
    with open(PATH + str(year) + "_thesis-link.txt", "r", encoding="latin1") as file: frequency[year] = len(file.readlines()) // 2

frequency = sorted([item for item in frequency.items()])
years, freq = np.array([year for year, freq in frequency]), np.array([freq for year, freq in frequency])

fig, ax = plt.subplots(figsize=(12,7))
ax.set_title("Number of bachelor's theses published per year", fontsize=18)
ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
ax.set_ylabel("Number of bachelor's theses published", fontsize=14)
ax.bar(years, height=freq, color="blue")
ax.legend(["Number of bachelor's theses published per year"], loc=2, fontsize=10)
fig.set_facecolor("lightcyan")
fig.savefig("Number_of_theses_published_per_year")