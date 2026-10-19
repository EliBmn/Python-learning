
# تعریف یک تابع برای تصمیم‌گیری درباره ایمیل
def classify_email(probability):

    # اگر احتمال فیشینگ کمتر از 0.20 باشد
    if probability < 0.20:
        return "Safe"

    # اگر احتمال فیشینگ بیشتر از 0.80 باشد
    elif probability > 0.80:
        return "Block"

    # در غیر این صورت بررسی انسانی لازم است
    else:
        return "Human Review"


# فراخوانی تابع برای سه ایمیل متفاوت
print(classify_email(0.10))
print(classify_email(0.55))
print(classify_email(0.95))
