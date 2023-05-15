import pandas as pd
import numpy as np
import isn_tractor.ibisn as it
import time


def dataframe(size, values):
    n_rows, n_cols = size
    mapped = "mapped" if "mapped" in values else "unmapped"

    if "discrete" in values:
        data = np.random.randint(0, 3, size=(n_rows, n_cols))
    elif "continuous" in values:
        data = np.random.uniform(0, 100, size=(n_rows, n_cols))
    else:
        raise ValueError("Values must contain either 'discrete' or 'continuous'")

    col_names = [mapped + "_" + "feature" + "_" + str(i) for i in range(n_cols)]
    index_names = ["sample_" + str(i) for i in range(n_rows)]

    df = pd.DataFrame(data, index=index_names, columns=col_names)

    return df

sizes = [
    (200, 1000),    
    (200, 2000),    
    (200, 3000),    
    (500, 1000),    
    (500, 2000),    
    (500, 3000),    
    (1000, 1000),    
    (1000, 2000),    
    (2000, 1000),]

times = []  # list to store processing times

for i, size in enumerate(sizes):
    df_name = f"m_df{i+1}"
    df = dataframe(size, ["mapped", "continuous"])
    start_time = time.time()
    it.dense_isn(df)
    end_time = time.time()
    times.append(end_time - start_time)
    df.to_csv(f"m_df{i+1}.csv", index=False)

times_df = pd.DataFrame({"processing_time": times})
times_df.to_csv("processing_times.csv", index=False)

print(times)
