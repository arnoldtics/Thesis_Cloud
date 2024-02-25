import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

PATH = "../DataCleaning/"

df = pd.read_csv(PATH+"Name_LastName_Title_Year.csv")

frequency = Counter(df["Year"])
for year in range(1840, 2025):
    if year not in frequency: frequency[year] = 0
frequency = sorted([item for item in frequency.items()], key=lambda x: x[0])

years = np.array([year for year, freq in frequency])
freq = np.array([freq for year, freq in frequency])

fig, ax = plt.subplots(figsize=(12,7))
ax.set_title("Plot of years vs bachelor's theses published", fontsize=18)
ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
ax.set_ylabel("Number of bachelor's theses published", fontsize=14)
ax.bar(years, height=freq, color="blue")
ax.legend(["Number of bachelor's theses published per year"], loc=2, fontsize=10)
fig.set_facecolor("lightblue")
fig.savefig("Number_of_theses_published_per_year")