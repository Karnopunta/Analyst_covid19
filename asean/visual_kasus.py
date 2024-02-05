import numpy as np
import pandas as pd
from kasus_dari_maret import df_covid_denormalized_asean_march_onward
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(16,6))
sns.lineplot(data=df_covid_denormalized_asean_march_onward, 
             x=df_covid_denormalized_asean_march_onward.index, 
             y="confirmed_cases", 
             hue="country_name",
             linewidth=2)
plt.xlabel('Record Date', fontsize=14)
plt.ylabel('Total Cases', fontsize=14)
plt.title('Comparison of COVID19 Cases in 5 ASEAN Countries', color="b", fontsize=18)
plt.grid()
plt.tight_layout()
plt.show()