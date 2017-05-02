import pandas as pd
import numpy as np

diagnosed_data = pd.read_json()

diagnosed_data = pd.get_dummies(diagnosed_data, columns=["DayName","WindDirection"])