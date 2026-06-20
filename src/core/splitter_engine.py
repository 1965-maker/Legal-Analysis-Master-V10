import os
import json

def split_and_route_judgment(json_data):
    metadata = json_data["court_judgment_analysis"]["metadata"]
    case_id = f"ruling_{metadata['case_number']}_{metadata['case_year'].replace(' ', '_').replace('ق', '')}"
    
    # تفكيك القواعد
    all_principles = json_data["court_judgment_analysis"]["abstract_legal_principles"]
    
    procedural_principles = []
    substantive_principles = []
    
    # الفرز بناءً على المسار المستهدف (Target Folder) الذي يحدده الـ Model
    for p in all_principles:
        if "procedural_law" in p.get("target_folder", ""):
            procedural_principles.append(p)
        else:
            substantive_principles.append(p)
            
    # تحديد مسارات الحفظ
    base_juris = "src/knowledge/jurisprudence"
    
    # 1. حفظ الملف الإجرائي إذا وجدت قواعد إجرائية
    if procedural_principles:
        # نأخذ أول مسار إجرائي كمقر رئيسي للملف
        target_subfolder = procedural_principles[0]["target_folder"]
        proc_path = os.path.join(base_juris, target_subfolder)
        os.makedirs(proc_path, exist_ok=True)
        
        proc_data = {
            "metadata": metadata,
            "search_tags": json_data["court_judgment_analysis"]["search_tags"],
            "court_correction_output": json_data["court_judgment_analysis"]["court_correction_output"],
            "abstract_legal_principles": procedural_principles
        }
        
        with open(os.path.join(proc_path, f"{case_id}.json"), "w", encoding="utf-8") as f:
            json.dump(proc_data, f, ensure_ascii=False, indent=2)
        print(f"✅ تم حفظ الشق الإجرائي في: {target_subfolder}")

    # 2. حفظ الملف الموضوعي إذا وجدت قواعد موضوعية
    if substantive_principles:
        target_subfolder = substantive_principles[0]["target_folder"]
        sub_path = os.path.join(base_juris, target_subfolder)
        os.makedirs(sub_path, exist_ok=True)
        
        sub_data = {
            "metadata": metadata,
            "search_tags": json_data["court_judgment_analysis"]["search_tags"],
            "referral_order": json_data["court_judgment_analysis"]["referral_order"],
            "verdict_logic": json_data["court_judgment_analysis"]["verdict_logic"],
            "case_facts": json_data["court_judgment_analysis"]["case_facts"],
            "appeal_grounds": json_data["court_judgment_analysis"]["appeal_grounds"],
            "abstract_legal_principles": substantive_principles,
            "court_correction_output": json_data["court_judgment_analysis"]["court_correction_output"]
        }
        
        with open(os.path.join(sub_path, f"{case_id}.json"), "w", encoding="utf-8") as f:
            json.dump(sub_data, f, ensure_ascii=False, indent=2)
        print(f"✅ تم حفظ الشق الموضوعي في: {target_subfolder}")
