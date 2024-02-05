import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from data import df_covid_denormalized

df_covid_denormalized["fatality_ratio"] = df_covid_denormalized["deaths"]/df_covid_denormalized["confirmed_cases"]
# print(df_covid_denormalized.head())

df_top_20_fatality_rate = df_covid_denormalized.sort_values("fatality_ratio", ascending=False).head(20)
print(df_top_20_fatality_rate[["geo_id","country_name","fatality_ratio"]])

#fatality Ratio on August
df_covid_denormalized_august = df_covid_denormalized.loc["2020-08"].groupby("country_name").sum()

df_covid_denormalized_august["fatality_ratio"] = df_covid_denormalized_august["deaths"]/df_covid_denormalized_august["confirmed_cases"]

df_top_20_fatality_rate_on_august = df_covid_denormalized_august.sort_values(by="fatality_ratio", ascending=False).head(20)
print(df_top_20_fatality_rate_on_august["fatality_ratio"])
