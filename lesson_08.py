
# Lesson 08 - Automatic ECE Calculation

# Predicted phishing probabilities
probabilities = [0.10, 0.20, 0.40, 0.60, 0.80, 0.90]

# Actual labels: 1 = Phishing, 0 = Legitimate
actual_labels = [0, 0, 1, 0, 1, 1]

# Probability ranges for the bins
bins = [(0.0, 0.3), (0.3, 0.7), (0.7, 1.01)]

total_emails = len(probabilities)
ece = 0

for lower, upper in bins:

    # Collect predictions and labels for this bin
    bin_predictions = []
    bin_labels = []

    for i in range(total_emails):

        if lower <= probabilities[i] < upper:
            bin_predictions.append(probabilities[i])
            bin_labels.append(actual_labels[i])

    # Skip bins with no emails
    if len(bin_predictions) == 0:
        continue

    # Average predicted phishing probability
    avg_prediction = sum(bin_predictions) / len(bin_predictions)

    # Actual phishing proportion
    actual_rate = sum(bin_labels) / len(bin_labels)

    # Calibration gap for this bin
    gap = abs(avg_prediction - actual_rate)

    # Weight based on number of emails in this bin
    weight = len(bin_predictions) / total_emails

    ece += weight * gap

    print("Bin:", lower, "-", upper)
    print("Average prediction:", round(avg_prediction, 2))
    print("Actual phishing rate:", round(actual_rate, 2))
    print("Gap:", round(gap, 2))
    print("------------------------")

print("Final ECE:", round(ece, 4))
