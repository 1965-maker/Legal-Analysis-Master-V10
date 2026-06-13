# محرك صياغة المذكرات - MASTER V10
def generate_legal_brief(case_data, nullity_findings):
    """
    يقوم هذا المحرك بدمج المعطيات (بيانات القضية + نتائج الفحص) 
    لصياغة الدفوع القانونية تلقائياً.
    """
    draft = f"""
    --- مـذكرة دفوع جنائية - MASTER V10 ---
    بناءً على القاعدة القانونية: {nullity_findings.get('basis', 'غير محدد')}
    الدفع الجوهري: {case_data.get('main_argument', 'لم يتم تحديد دفع')}
    ---------------------------------------
    توقيع: سيادة المستشار - MASTER V10 Engine
    """
    return draft

# اختبار المحرك
print(generate_legal_brief({"main_argument": "الدفع ببطلان القبض والتفتيش"}, {"basis": "المادة 334 إجراءات جنائية"}))
