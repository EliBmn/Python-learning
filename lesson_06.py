
# احتمال فیشینگ پیش‌بینی‌شده برای 100 ایمیل
predicted_probabilities = [0.95] * 100

# برچسب واقعی: 80 ایمیل فیشینگ، 20 ایمیل سالم
actual_labels = [1] * 80 + [0] * 20

# میانگین احتمال اعلام‌شده مدل
average_prediction = (
    sum(predicted_probabilities) / len(predicted_probabilities)
)

# نرخ واقعی فیشینگ
actual_rate = sum(actual_labels) / len(actual_labels)

# اختلاف بین احتمال پیش‌بینی‌شده و نرخ واقعی
calibration_gap = abs(average_prediction - actual_rate)

print("Predicted probability:", average_prediction)
print("Actual phishing rate:", actual_rate)
print("Calibration gap:", round(calibration_gap, 2))
