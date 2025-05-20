# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# PATH, frequency = "../DataCleaning/", {}

# df = pd.read_csv(PATH + "Name_LastName_Title_Year.csv")
# for year in df["Year"].unique():
#     frequency[year] = df[df["Year"] == year].shape[0]

# years, freq = np.array([year for year, freq in frequency.items()]), np.array([freq for year, freq in frequency.items()])

# fig, ax = plt.subplots(figsize=(12,7))
# ax.set_title("Number of bachelor's theses published per year", fontsize=18)
# ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
# ax.set_ylabel("Number of bachelor's theses published", fontsize=14)
# ax.bar(years, height=freq, color="blue")
# ax.legend(["Number of bachelor's theses published per year"], loc=2, fontsize=10)
# fig.set_facecolor("lightcyan")
# fig.savefig("Number_of_theses_published_per_year")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
PATH, frequency = "../DataCleaning/", {}

df = pd.read_csv(PATH + "Name_LastName_Title_Year.csv")
for year in df["Year"].unique():
    frequency[year] = df[df["Year"] == year].shape[0]

years = np.array(sorted(frequency.keys()))
freq = np.array([frequency[year] for year in years])

fig, ax = plt.subplots(figsize=(12,7))
ax.set_title("Number of bachelor's theses published per year", fontsize=18)
ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
ax.set_ylabel("Number of bachelor's theses published", fontsize=14)
sns.histplot(df["Year"], color="blue", discrete=True, ax=ax)
ax.set_yticks(np.arange(0, 10001, 1000))
ax.legend(["Number of bachelor's theses published per year"], loc=2, fontsize=10)
fig.set_facecolor("lightcyan")
fig.savefig("Number_of_theses_published_per_year")