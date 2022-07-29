import pandas as pd
df = pd.read_csv("employees.csv")
print(df.iloc[3:6,0:5])

dict = {
    "names" :["loca", "kika", "jiji"],
    "ages" :[15, 26, 22]
}

df = pd.DataFrame(dict)
print(df)

