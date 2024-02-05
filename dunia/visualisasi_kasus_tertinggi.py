# Visulisasi
import matplotlib.pyplot as plt
from fatal_ratio import df_top_20_fatality_rate_on_august
plt.figure(figsize=(8,8))
df_top_20_fatality_rate_on_august["fatality_ratio"].sort_values().plot(kind="barh", color="yellow")
plt.title("Top 20 Highest Fatality Rate Countries", fontsize=18, color="black")
plt.xlabel("Fatality Rate", fontsize=14)
plt.ylabel("Country Name", fontsize=14)
plt.grid(axis="x")
plt.tight_layout()
plt.show()
