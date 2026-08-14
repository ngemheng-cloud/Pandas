import pandas as pd

file_path = "earthquake.csv"

df = pd.read_csv(file_path)
print("--- Data successfully loaded ---\n")

print("=== 1. First 5 Rows (.head()) ===")
print(df.head(), "\n")

print("=== 2. Dataset Structure & Data Types (.info()) ===")
df.info()
print("\n")

print("=== 3. Summary Statistics for Numeric Columns (.describe()) ===")
print(df.describe(), "\n")

print("=== 4. Regions with Most Frequent Seismic Activity ===")

location_counts = df['place'].value_counts()
print(location_counts.head(10), "\n")

 
magnitude_series = df['mag']

print("=== Series vs. DataFrame Demonstration ===")
print(f"Object Type for df: {type(df)}")
print(f"Object Type for magnitude_series: {type(magnitude_series)}")
print(f"Magnitude Series Summary:\nMean: {magnitude_series.mean():.2f} | Max: {magnitude_series.max():.2f}\n")


locations = df['place']


df_sorted = df.sort_values(by='mag', ascending=False)


top_5_earthquakes = df_sorted.iloc[0:5]

print("=== Top 5 Largest Earthquakes ===")
print(top_5_earthquakes[['place', 'mag', 'depth', 'time']])
print("\n")

japan_or_texas_high_mag = df[
    (df['mag'] > 6.0) & 
    ((df['place'].str.contains('Japan', case=False, na=False)) | 
     (df['place'].str.contains('Texas', case=False, na=False)))
]

print("=== Filtered Results: Mag > 6.0 in Japan or Texas ===")
print(japan_or_texas_high_mag[['place', 'mag', 'depth']])

# Export filtered subset to Excel for analysis report
japan_or_texas_high_mag.to_excel("filtered_earthquakes_high_risk.xlsx", index=False)

# Export filtered subset to JSON for web developer team consumption
japan_or_texas_high_mag.to_json("filtered_earthquakes_web.json", orient="records", indent=4)

print("--- Filtered results exported to Excel and JSON successfully ---")