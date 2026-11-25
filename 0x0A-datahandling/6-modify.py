# a program to modify data frame

import pandas as pd
# df means dataframe

data = {
    "names": ["Abdul", "Asmau", "Caleb", "John"],
    "state": ["Kogi", "Zamfara", "Akwaibom", "Gombe"],
    "Age": [18, 21, 19, 24],
    "specialization": ["cooking", "Enginner", "Boxing", "High flyer"]
}
df = pd.DataFrame(data)

df["state"] = df["state"].replace("Akwaibom", "Akwa ibom")
df["specialization"] = df["specialization"].replace("Enginner", "Engineer")
print(df.head())

df["state"] = df["state"].str.upper()
print(df.head())