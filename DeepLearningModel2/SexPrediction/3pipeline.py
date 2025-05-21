import torch 
import pandas as pd
import os 
from transformers import pipeline

path = "../../DataCleaning/"

df = pd.read_csv(path + "Name_LastName_Title_Year.csv")

# Some registers have the name in the last name
df["Name"].fillna(df["Last Name"], inplace=True)

# To predict the sex of a person based on his/her name
classifier = pipeline("zero-shot-classification", # zero-shot classification allows to create our own categories
                      model="facebook/bart-large-mnli", # selection of the model
                      device="cuda") # running everything on cuda

# Processing the names in batch, not directly on the dataframe
names = df["Name"].unique().tolist()
candidate_labels = ["man", "woman"]
results = classifier(names, candidate_labels) 
# results is a list of dictionaries, each one for a instance

# Extract the results
name_to_sex = {}
for name, res in zip(names, results):
    # Verify the score for both categories
    man_score = res["scores"][res["labels"].index("man")]
    woman_score = res["scores"][res["labels"].index("woman")]
    # The category will only be taken in consideration if the model has 65% or more confidence on the answer
    if man_score >= 0.65:
        name_to_sex[name] = "male"
    elif woman_score >= 0.65:
        name_to_sex[name] = "female"
    else:
        name_to_sex[name] = "unsure"

# Mapping the answer
df["Sex"] = df["Name"].map(name_to_sex)

# Saving the dataset
df.to_csv("Dataset_with_sex.csv", index=False)