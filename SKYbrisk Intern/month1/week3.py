# WEEK 3 – NUMPY & PANDAS

import numpy as np
import pandas as pd

arr = np.array([10,20,30,40])
print(np.mean(arr))
print(arr**2)

data = {
    "Name": ["A","B","C","D"],
    "Marks": [80,None,75,90]
}

df = pd.DataFrame(data)
df = df.dropna()
print(df)
print(df["Marks"].mean())
