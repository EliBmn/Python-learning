
# Lesson 12 - Save decisions to CSV

import pandas as pd

# Simulated model outputs
results = [
    {"email_id": 1, "isPhishing": True, "confidence": 0.95},
    {"email_id": 2, "isPhishing": False, "confidence": 0.90},
    {"email_id": 3, "isPhishing": True, "confidence": 0.65},
    {"email_id": 4, "isPhishing": False, "confidence": 0.60}
]

T_SAFE = 0.20
T_PHISH = 0.80

records = []

for result in results:

    confidence = result["confidence"]
    is_phishing = result["isPhishing"]

    # Convert confidence to a phishing score
    if is_phishing:
        phishing_score = confidence
    else:
        phishing_score = 1 - confidence

    # Choose the simulated action
    if phishing_score < T_SAFE:
        action = "SAFE"
    elif phishing_score >= T_PHISH:
        action = "BLOCK"
    else:
        action = "HUMAN REVIEW"

    # Store one record for each email
    records.append({
        "email_id": result["email_id"],
        "isPhishing": is_phishing,
        "confidence": confidence,
        "phishing_score": round(phishing_score, 2),
        "action": action
    })

# Convert records into a table
df = pd.DataFrame(records)

# Save the table as a CSV file
df.to_csv("calibraphish_results.csv", index=False)

print(df)
print("Results saved successfully!")
