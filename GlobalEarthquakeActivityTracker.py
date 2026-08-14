import pandas as pd
# 1. DATA I/O: Loading the Dataset
file_path = "earthquake.csv"
# Load the earthquake dataset into a Pandas DataFrame
df = pd.read_csv(file_path)
print("--- Data successfully loaded ---\n")
#2. DATA INSPECTION
print("=== 1. First 5 Rows (.head()) ===")
print(df.head(), "\n")

print("=== 2. Dataset Structure & Data Types (.info()) ===")
df.info()
print("\n")

print("=== 3. Summary Statistics for Numeric Columns (.describe()) ===")
print(df.describe(), "\n")

print("=== 4. Regions with Most Frequent Seismic Activity ===")
# Frequency count of earthquake occurrences by place
location_counts = df['place'].value_counts()
print(location_counts.head(10), "\n")

 # 3.DATA STRUCTURES: DataFrame (2D) vs. Series (1D)

# Isolate the magnitude column as a 1D Pandas Series
magnitude_series = df['mag']

print("=== Series vs. DataFrame Demonstration ===")
print(f"Object Type for df: {type(df)}")
print(f"Object Type for magnitude_series: {type(magnitude_series)}")
print(f"Magnitude Series Summary:\nMean: {magnitude_series.mean():.2f} | Max: {magnitude_series.max():.2f}\n")


# 4. INDEXING AND SELECTION
# Column Selection using dictionary-style bracket notation
locations = df['place']

# Sort dataset by magnitude descending to rank largest earthquakes
df_sorted = df.sort_values(by='mag', ascending=False)

# Use .iloc[] to extract the top 5 largest earthquakes based on row position (0 to 4)
top_5_earthquakes = df_sorted.iloc[0:5]

print("=== Top 5 Largest Earthquakes ===")
print(top_5_earthquakes[['place', 'mag', 'depth', 'time']])
print("\n")
# 5. FILTERING WITH MULTIPLE BOOLEAN CONDITIONS
# Filter criteria: Magnitude > 6.0 AND occurring in either "Japan" OR "Texas"
# Note: Wrapping conditions in parentheses () is required when using & and |
japan_or_texas_high_mag = df[
    (df['mag'] >6.0) & 
    ((df['place'].str.contains('Japan', case=False, na=False)) | 
     (df['place'].str.contains('Texas', case=False, na=False)))
]

print("=== Filtered Results: Mag > 6.0 in Japan or Texas ===")
print(japan_or_texas_high_mag[['place', 'mag', 'depth']])

# 6. DATA I/O: Exporting Filtered Findings

# Export filtered subset to Excel for analysis report
japan_or_texas_high_mag.to_excel("filtered_earthquakes_high_risk.xlsx", index=False)

# Export filtered subset to JSON for web developer team consumption
japan_or_texas_high_mag.to_json("filtered_earthquakes_web.json", orient="records", indent=4)

print("--- Filtered results exported to Excel and JSON successfully ---")