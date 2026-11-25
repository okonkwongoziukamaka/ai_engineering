# a program to write data from the scratch

import pandas as pd

data = {
    "title": ["Introduction to AI", "RAG System", "Prompt Engineering"],
    "word_count": [1500, 3000, 3500],
    "category": ["Basic", "Advance", "Basics"],
}
df = pd.DataFrame(data)
title = df["title"]
first_row = df.iloc[0]
row_by_label = df.loc[0]
print(title)
print(first_row)
print(row_by_label)