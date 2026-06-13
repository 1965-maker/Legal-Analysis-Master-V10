# نظام MASTER V10 - المركز الرئيسي
from src.agents.client_intake import conduct_intake_interview
from src.agents.drafting_engine import generate_legal_brief
from src.agents.case_roi import calculate_case_roi

def run_master_v10_system(client_text):
    print("--- بدء تشغيل منظومة MASTER V10 ---")
    
    # 1. تحليل مقابلة العميل
    intake_result = conduct_intake_interview(client_text)
    print(intake_result)
    
    # 2. تقييم الجدوى
    roi = calculate_case_roi(0.8, 50000, 20)
    print(f"الجدوى الاستراتيجية: {roi}")
    
    # 3. صياغة المذكرة
    brief = generate_legal_brief({"main_argument": "الدفع ببطلان القبض"}, {"basis": "م 334 إ.ج"})
    print(brief)
    
    print("--- تم إتمام العمليات بنجاح ---")

# تشغيل النظام
run_master_v10_system("واقعة القبض على المتهم الساعة 10 مساءً دون إذن")
