# محرك تقييم المخاطر والـ KPIs - MASTER V10
def calculate_case_kpi(nullity_score, evidence_strength):
    """
    يقوم هذا المحرك بحساب مؤشر قوة القضية (Case Strength Index)
    من خلال دمج نقاط البطلان المكتشفة مع قوة الأدلة.
    """
    # معادلة تقييم مبدئية: قوة القضية تعتمد على حجم البطلان المكتشف
    case_strength = (nullity_score * 0.7) + (evidence_strength * 0.3)
    
    risk_level = "High" if case_strength < 50 else "Low"
    
    return {
        "case_strength_index": case_strength,
        "risk_level": risk_level,
        "status": "تم تحليل مؤشرات الأداء بنجاح"
    }

# اختبار المحرك: (بطلان مرتفع 80، قوة أدلة خصم 40)
print(calculate_case_kpi(80, 40))
