
import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "data.xlsx")

df = pd.read_excel(file_path)
