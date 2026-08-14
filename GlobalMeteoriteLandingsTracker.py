import pandas as pd

# Load the earthquake dataset into a Pandas DataFrame
df = pd.read_csv("meteorites.csv")

print("--- 1. First 5 Rows (head) ---")
print(df.head())
print("\n" + "="*50 + "\n")

print("--- 2. Dataset Info (info) ---")
df.info()
print("\n" + "="*50 + "\n")

print("--- 3. Summary Statistics (describe) ---")
print(df.describe())
print("\n" + "="*50 + "\n")

print("--- 4. Most Frequent Meteorite Classifications ---")
print(df['classification'].value_counts())
print("\n" + "="*50 + "\n")

mass_series = df['mass_grams']

print("--- Mass Series (1D Data Structure) ---")
print(type(mass_series))
print(mass_series.head())
print("\n" + "="*50 + "\n")

# Dictionary-style selection for a specific column
fall_status = df["fall_status"]
print("--- Dictionary-style Selection: fall_status ---")
print(fall_status.head())
print("\n" + "="*50 + "\n")

df_sorted_by_mass = df.sort_values(by="mass_grams", ascending=False)

top_5_heaviest = df_sorted_by_mass.iloc[0:5]

print("--- Top 5 Heaviest Meteorites (iloc) ---")
print(top_5_heaviest)
print("\n" + "="*50 + "\n")

condition_mass = df['mass_grams'] > 50000
condition_region = (df['region'] == "Antarctica") | (df['region'] == "Sahara")

filtered_meteorites = df[condition_mass & condition_region]

print("--- Filtered Meteorites (> 50k grams & Antarctica/Sahara) ---")
print(filtered_meteorites)
print("\n" + "="*50 + "\n")

filtered_meteorites.to_excel("museum_exhibit_meteorites.xlsx", index=False)
filtered_meteorites.to_json("museum_exhibit_meteorites.json", orient="records", indent=4)

print("Filtered results successfully exported to Excel and JSON!")