
# Lesson 11 - Safe Offline Decision Layer

# Example outputs (not real model predictions)
results = [
    {"isPhishing": True, "confidence": 0.95},
    {"isPhishing": False, "confidence": 0.90},
    {"isPhishing": True, "confidence": 0.65},
    {"isPhishing": False, "confidence": 0.60}
]

T_SAFE = 0.20
T_PHISH = 0.80

for result in results:

    is_phishing = result["isPhishing"]
    confidence = result["confidence"]

    # Convert label confidence to a phishing score
    if is_phishing:
        phishing_score = confidence
    else:
        phishing_score = 1 - confidence

    # Decide without deleting or moving emails
    if phishing_score < T_SAFE:
        action = "SAFE"
    elif phishing_score >= T_PHISH:
        action = "BLOCK"
    else:
        action = "HUMAN REVIEW"

    print("Phishing score:", round(phishing_score, 2))
    print("Decision:", action)
    print("------------------------")

