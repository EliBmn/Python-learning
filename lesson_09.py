
# Lesson 09 - Reliability Diagram

import matplotlib.pyplot as plt

# Average predicted phishing probability per bin
predicted = [0.15, 0.50, 0.85]

# Actual phishing rate per bin
actual = [0.00, 0.50, 1.00]

# Draw the ideal calibration line
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Perfect Calibration"
)

# Draw the model's actual calibration results
plt.plot(
    predicted,
    actual,
    marker="o",
    label="Our Model"
)

# Add labels to the chart
plt.xlabel("Predicted Phishing Probability")
plt.ylabel("Actual Phishing Rate")
plt.title("Reliability Diagram")

# Set axis limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Show legend and grid
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig("reliability_diagram.png", dpi=300)

# Display the chart
plt.show()

