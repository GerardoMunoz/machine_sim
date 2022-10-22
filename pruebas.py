import pandas as pd
import numpy as np

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(3)), dtype="float32"),
        "D": np.array([3] * 3, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test"]),
        "F": "foo",
    }
)

keys=df2.keys()
print(df2,end="\n\n")
print(keys,end="\n\n")
print(df2.T)