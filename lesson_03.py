
# تابع تشخیص وضعیت ایمیل
def classify_email(probability):
    if probability < 0.20:
        return "Safe"
    elif probability >= 0.80:
        return "Block"
    else:
        return "Human Review"


# یک لیست شامل احتمال فیشینگ پنج ایمیل
emails = [0.10, 0.45, 0.90, 0.20, 0.85]

# بررسی تک‌تک ایمیل‌ها
for probability in emails:

    # فرستادن احتمال هر ایمیل به تابع
    result = classify_email(probability)

    # نمایش احتمال و نتیجه
    print(probability, "->", result)
