"""Lesson 1: Three-way phishing decisions (educational example, NOT real detection)."""

# This number is invented for practice. It does NOT come from an AI model.
phishing_probability = 0.95

# Thresholds are also illustrative; research will estimate them from real data.
safe_threshold = 0.20
phishing_threshold = 0.80

# Sanity check: the safe threshold must be below the phishing threshold.
assert 0 <= safe_threshold < phishing_threshold <= 1

# Python checks the conditions from top to bottom.
if phishing_probability < safe_threshold:
    decision = "Safe email"
elif phishing_probability > phishing_threshold:
    decision = "Potential phishing: simulated block"
else:
    decision = "Needs human review"

# print() displays the result in the terminal.
print("Phishing probability:", phishing_probability)
print("Decision:", decision)
print("My first GitHub project")
git add lesson_01.py
# Practice: change phishing_probability to 0.10, then 0.95, and rerun.
