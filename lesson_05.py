
# تابع تصمیم‌گیری
def classify_email(probability):
    if probability < 0.20:
        return "Safe"
    elif probability >= 0.80:
        return "Block"
    else:
        return "Human Review"


# داده‌های فرضی
emails = [0.10, 0.45, 0.90, 0.20, 0.85, 0.99]

# شمارنده‌ها
safe_count = 0
block_count = 0
review_count = 0

# بررسی ایمیل‌ها
for probability in emails:
    result = classify_email(probability)

    if result == "Safe":
        safe_count += 1
    elif result == "Block":
        block_count += 1
    else:
        review_count += 1


# تعداد کل ایمیل‌ها
total_emails = len(emails)

# درصد ایمیل‌هایی که انسان باید بررسی کند
review_rate = (review_count / total_emails) * 100

# درصد ایمیل‌هایی که خودکار مدیریت می‌شوند
automation_rate = ((safe_count + block_count) / total_emails) * 100

# نمایش نتایج
print("Total emails:", total_emails)
print("Human Review Rate:", round(review_rate, 2), "%")
print("Automation Rate:", round(automation_rate, 2), "%")
