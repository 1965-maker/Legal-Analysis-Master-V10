# محرك تقييم العائد الاستثماري للقضية - MASTER V10
def calculate_case_roi(success_probability, legal_fees, effort_hours):
    """
    يقوم هذا المحرك بحساب مؤشر جدوى القضية (Case ROI)
    success_probability: نسبة نجاح القضية (0-1)
    legal_fees: الأتعاب المتوقعة
    effort_hours: عدد ساعات العمل المتوقعة
    """
    roi_score = (success_probability * legal_fees) / (effort_hours + 1)
    
    return {
        "roi_score": round(roi_score, 2),
        "decision": "قبول القضية" if roi_score > 500 else "إعادة تقييم"
    }

# اختبار المحرك: (احتمال نجاح 80%، أتعاب 50000، جهد 40 ساعة)
print(calculate_case_roi(0.8, 50000, 40))
