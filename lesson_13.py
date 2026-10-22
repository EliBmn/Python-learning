
import pandas as pd

# Read the CSV file created in lesson 12
df = pd.read_csv("calibraphish_results.csv")

# Show the entire table
print("Our dataset:")
print(df)

# Count each type of decision
print("\nDecision counts:")
print(df["action"].value_counts())

# Calculate the average phishing score
average_score = df["phishing_score"].mean()

print("\nAverage phishing score:", average_score)
