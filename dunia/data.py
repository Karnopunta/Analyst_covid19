import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

covid_url = "https://storage.googleapis.com/dqlab-dataset/covid19_worldwide_2020.json"
df_covid_worldwide = pd.read_json(covid_url)

# print("Ukuran dataset: %d kolom dan %d baris.\n" % df_covid_worldwide.shape)
# print("Lima data teratas:\n", df_covid_worldwide.head())
# print("\nLima data terbawah:\n", df_covid_worldwide.tail())
countries_url = "https://storage.googleapis.com/dqlab-dataset/country_details.json"
df_countries = pd.read_json(countries_url)
# print(df_countries.head())

df_covid_denormalized = pd.merge(df_covid_worldwide.reset_index(), df_countries, on="geo_id").set_index("date")
# print(df_covid_denormalized.head())