# MASTER V10 – Architecture Overview

## 1. Design Philosophy
MASTER V10 يعتمد على منهجية **Domain‑Centric + Cross‑Cutting Architecture**.
كل مجال قانوني (جنائي، مدني، أحوال، ضرائب، اقتصادي...) يُبنى كمحرك مستقل يحتوي على كل عناصره الموضوعية والإجرائية، بينما القواعد المشتركة (المرافعات، البطلان، الإجراءات العامة) تُخزَّن في طبقة عرضية مشتركة ويُحقن استخدامها عند الحاجة عبر الـ Orchestrator.

## 2. Core Layers
- **Domain Engines:** محركات القوانين (جنائي، مدني، أحوال، ضرائب، اقتصادي، شركات، عمل، تأمينات).
- **General Engines:** محركات عامة (Client Interview, Risk, Defense, Contracts, Pleadings, Judicial Memory, Judgment Analysis).
- **Cross‑Cutting Layer:** قواعد الإجراءات والبطلان المشتركة.
- **Orchestrator:** العقل المنسق بين كل المحركات، يحدد السياق ويستدعي القواعد المناسبة.
- **Docs Layer:** وثائق التصميم والمراجع القانونية.

## 3. Data Model
كل قاعدة قانونية تُخزَّن بصيغة JSON موحدة:
```json
{
  "id": "rule_id",
  "domain": "criminal",
  "source_law": "Penal Code",
  "article": "مادة 123",
  "rule_type": "substantive | procedural | public_order | nullity",
  "topic": "attempt | complicity | custody | ...",
  "conditions": [],
  "effects": [],
  "references": []
}
