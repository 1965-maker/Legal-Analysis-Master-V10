# محرك كشف البطلان - MASTER V10
def detect_nullity(error_type):
    """
    يقوم هذا المحرك بتصنيف العيب الإجرائي وفقاً 
    للقواعد التي قررناها: (انعدام، نظام عام، نسبي).
    """
    nullity_levels = {
        "absolute": "بطلان متعلق بالنظام العام - م 334",
        "relative": "بطلان نسبي - م 335",
        "non_existent": "عمل منعدم - لا يرتب أثراً"
    }
    return nullity_levels.get(error_type, "تصنيف غير معروف")

# اختبار المحرك
print(detect_nullity("absolute"))
