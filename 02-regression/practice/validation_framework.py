import pandas as pd
import numpy as np

path = "https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv"

# Load the data
df = pd.read_csv(path)

# Split the data
n = len(df)

n_val = int(n * 0.2)
n_test = int(n * 0.2)
n_train = n - n_val - n_test

print(
    f"Total: {n}, "
    f"Validation: {n_val}, "
    f"Test: {n_test}, "
    f"Train: {n_train}"
)

# Shuffle the data
np.random.seed(2)
idx = np.arange(n)
np.random.shuffle(idx)

# Split the data
df_train = df.iloc[idx[:n_train]]
df_test = df.iloc[idx[n_train:n_train + n_test]]
df_val = df.iloc[idx[n_train + n_test:]]

# Reset indices
df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

print(df_test.head())