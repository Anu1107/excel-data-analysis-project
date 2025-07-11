import pandas as pd
import numpy as np
df= pd.read_csv("C:/Users/Shiv/OneDrive/Desktop/code/.vscode/Notes/Python/messy_hr_data.csv")

df.loc[4, ["name","email","age","join_date"]]= ["Robin hood", "robin.hood@gamil.com", 32, "24/08/2021"]
df.loc[7, ["name","join_date","dept"]]= ["Aditya", "11/02/2022","IT"]
df.loc[2, ["age"]] = [25]

df["status"].fillna("Left", inplace= True)

df["salary"] = df["salary"].astype(str).str.replace(",", "").str.replace("$", "")
df["salary"]= pd.to_numeric(df["salary"], errors='coerce')

ass= df["salary"].mean()
df["salary"].fillna(ass, inplace= True)
df["salary"]= df["salary"].round(2)

df["status"]= df["status"].str.capitalize()
df["name"]= df["name"].str.title()

print(df)
