
import pandas as pd

# Simulated labeled examples
data = [
    {"email_id": 1, "actual": 1, "predicted": 1},
    {"email_id": 2, "actual": 0, "predicted": 0},
    {"email_id": 3, "actual": 1, "predicted": 0},
    {"email_id": 4, "actual": 0, "predicted": 1},
    {"email_id": 5, "actual": 1, "predicted": 1},
    {"email_id": 6, "actual": 0, "predicted": 0}
]

df = pd.DataFrame(data)

# 1 = Phishing, 0 = Legitimate

TP = ((df["actual"] == 1) & (df["predicted"] == 1)).sum()
TN = ((df["actual"] == 0) & (df["predicted"] == 0)).sum()
FP = ((df["actual"] == 0) & (df["predicted"] == 1)).sum()
FN = ((df["actual"] == 1) & (df["predicted"] == 0)).sum()

print("True Positive:", TP)
print("True Negative:", TN)
print("False Positive:", FP)
print("False Negative:", FN)
