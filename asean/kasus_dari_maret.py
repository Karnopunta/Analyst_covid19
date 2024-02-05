import numpy as np
import pandas as pd
#pd.set_option("display.max_columns", None)
from data import df_covid_denormalized_asean

df_covid_denormalized_asean_march_onward = df_covid_denormalized_asean[df_covid_denormalized_asean.index>="2020-03-01"]
print(df_covid_denormalized_asean_march_onward.head(5))