import numpy as np
import pandas as pd

df = pd.read_csv("path_to_file");

set_dtypes = {};

int_dtypes = ['int8', 'int16', 'int32', 'int64']
float_dtypes = ['float16', 'float32', 'float64']

k_min, k_max = 0, 0
for j in df.columns:
    if df[j].dtype != object:
        m = max(abs(df[j]))
        for i in int_dtypes:
            k_max = np.iinfo(i).max
            k_min = np.iinfo(i).min
            if np.dtype(df[j])==int and (m>k_min and m<k_max):
                set_dtypes[j] = i
                break
        for i in float_dtypes:
            k_max = np.finfo(i).max
            k_min = np.finfo(i).min 
            if np.dtype(df[j])==float and (m>k_min and m<k_max):
                set_dtypes[j] = i
                break