import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
PATH = "../DeepLearningModel2/SexPrediction/"

df = pd.read_csv(PATH + "Dataset_with_sex.csv")



# HISTOGRAM
order = ["male", "female", "unsure"]
palette = {"male": "forestgreen", "female": "darkviolet", "unsure": "crimson"}

fig, ax = plt.subplots(figsize=(12, 7))
ax.set_title("Number of bachelor's theses published per sex", fontsize=18)
ax.set_xlabel("Sex", fontsize=14)
ax.set_ylabel("Number of bachelor's theses published", fontsize=14)

sns.countplot(
    data=df,
    x="Sex",
    hue="Sex",
    palette=palette,
    order=order,
    legend=False,
    ax=ax,
)

ax.legend(title="Sex", labels=order, loc=1, fontsize=10)
fig.set_facecolor("lightcyan")
fig.show()
fig.savefig("Number_of_theses_published_per_sex")



# MEN
men = df[df["Sex"] == "male"]
men = men.sort_values(by="Sex")
fig, ax = plt.subplots(figsize=(12,7))
ax.set_title("Number of bachelor's theses by men published per year", fontsize=18)
ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
ax.set_ylabel("Number of bachelor's theses by men published", fontsize=14)
sns.histplot(men['Year'], color="forestgreen", discrete=True, ax=ax)
ax.set_yticks(np.arange(0, 10001, 1000))
ax.legend(["Number of bachelor's theses by men published per year"], loc=2, fontsize=10)
fig.set_facecolor("lightcyan")
fig.savefig("Number_of_theses_published_per_year_men")



# WOMEN
women = df[df["Sex"] == "female"]
women = women.sort_values(by="Sex")
fig, ax = plt.subplots(figsize=(12,7))
ax.set_title("Number of bachelor's theses by women published per year", fontsize=18)
ax.set_xlabel("Years from 1840 to 2024", fontsize=14)
ax.set_ylabel("Number of bachelor's theses by women published", fontsize=14)
sns.histplot(women['Year'], color="darkviolet", discrete=True, ax=ax)
ax.set_yticks(np.arange(0, 10001, 1000))
ax.legend(["Number of bachelor's theses by women published per year"], loc=2, fontsize=10)
fig.set_facecolor("lightcyan")
fig.savefig("Number_of_theses_published_per_year_women")



# SEX
# Preprocessing
grouped = df.groupby(["Year", "Sex"]).size().unstack(fill_value=0)
grouped = grouped[["male", "female", "unsure"]]  # order of stack

years = grouped.index.to_numpy()
bar_width = 1 

x = np.arange(len(years))

colors = {
    "male": "forestgreen",
    "female": "darkviolet",
    "unsure": "indianred"
}

fig, ax = plt.subplots(figsize=(12, 7))

bottom = np.zeros_like(years)

for sex in ["male", "female", "unsure"]:
    heights = grouped[sex].values
    ax.bar(x, heights, bottom=bottom, color=colors[sex], label=sex, width=bar_width)
    bottom += heights  # stacking

# Style
ax.set_title("Number of bachelor's theses published per year by sex", fontsize=18)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of bachelor's theses", fontsize=14)
ax.legend(title="Sex", fontsize=10, loc='upper left')
ax.set_facecolor("white")
fig.set_facecolor("lightcyan")

# Ticks
step = max(1, len(x) // 20)
ax.set_xticks(x[::step])
ax.set_xticklabels(years[::step], rotation=0)

fig.tight_layout()
fig.savefig("Number_of_theses_published_per_year_sex")