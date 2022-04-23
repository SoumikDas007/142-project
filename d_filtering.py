import numpy as np
import csv
import pandas as pd

data1 = pd.read_csv("final.csv")


data1 = data1.sort_values("total_events",ascending = False)
data1.head(20).values.tolist()
