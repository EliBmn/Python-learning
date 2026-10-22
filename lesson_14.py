
import pandas as pd

# Read results from lesson 12
df = pd.read_csv("calibraphish_results.csv")

# Total number of emails
total = len(df)

# Count emails sent to human review
review_count = (df["action"] == "HUMAN REVIEW").sum()

# Count automatically handled emails
automation_count = total - review_count

# Calculate percentages
review_rate = review_count / total * 100
automation_rate = automation_count / total * 100

print("Total emails:", total)
print("Human reviews:", review_count)
print("Automated decisions:", automation_count)
print("Review rate:", review_rate, "%")
print("Automation rate:", automation_rate, "%")
