# محرك التكييف القانوني - MASTER V10
import json

def load_penal_data(part):
    """
    يقوم هذا المحرك بجلب القواعد من المجلد الذي أنشأناه
    """
    path = f"src/domains/criminal/rules/penal_code_data/{part}.json"
    # سنقوم لاحقاً بتفعيل وظيفة القراءة الفعلية للملفات
    return f"تم تحميل البيانات من {path}"

# اختبار الربط
print(load_penal_data("general_part"))
print(load_penal_data("special_part"))
