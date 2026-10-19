
# تابع تصمیم‌گیری درباره ایمیل
def classify_email(probability):
    if probability < 0.20:
        return "Safe"
    elif probability >= 0.80:
        return "Block"
    else:
        return "Human Review"


# احتمال فیشینگ شش ایمیل فرضی
emails = [0.10, 0.45, 0.90, 0.20, 0.85, 0.99]

# شمارنده‌ها را ابتدا صفر می‌کنیم
safe_count = 0
block_count = 0
review_count = 0

# بررسی تمام ایمیل‌ها
for probability in emails:

    result = classify_email(probability)

    # شمارنده مربوط به هر نتیجه را افزایش می‌دهیم
    if result == "Safe":
        safe_count += 1

    elif result == "Block":
        block_count += 1

    else:
        review_count += 1


# نمایش نتیجه نهایی
print("Safe:", safe_count)
print("Blocked:", block_count)
print("Human Review:", review_count)
