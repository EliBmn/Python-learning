
# Lesson 07 - Expected Calibration Error

# Average predicted phishing probability in each group
predicted = [0.20, 0.60, 0.90]

# Actual proportion of phishing emails in each group
actual = [0.10, 0.50, 0.70]

# Number of emails in each group
counts = [10, 10, 10]

total_emails = sum(counts)
weighted_error = 0

for i in range(len(predicted)):
    gap = abs(predicted[i] - actual[i])
    weighted_error += gap * counts[i]

    print("Group", i + 1, "gap:", round(gap, 2))

ece = weighted_error / total_emails

print("ECE:", round(ece, 4))
