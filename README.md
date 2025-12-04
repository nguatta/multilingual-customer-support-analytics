 🌍 Multilingual Customer Support Analytics
> 31% ↑ Customer Satisfaction | 30% ↓ Resolution Time | 210+ Tickets Analyzed

[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?logo=powerbi)](https://github.com/nguatta/multilingual-customer-support-analytics)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?logo=linkedin)](https://linkedin.com/in/ake-marc-albert-adje-5b341a110)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_More-4285F4)](https://datascienceportfol.io/akemarcpt)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL-316192?logo=postgresql)](https://www.postgresql.org/)



 📊 Project Overview

Companies operating in multilingual markets struggle to optimize customer satisfaction due to inefficient language pairing between agents and customers. This project analyzes 210+ support tickets across 5 languages to quantify the business impact of language matching.

 🎯 Key Finding
Matching customer-agent languages increases satisfaction by 31% and reduces resolution time by 30% — translating to significant cost savings and improved customer experience.



 💼 Business Problem

- Inefficient routing: Tickets assigned without considering language preferences
- Lack of data-driven insights: No quantitative metrics on language impact  
- Unknown ROI: Unclear business case for multilingual hiring investments
- Customer churn risk: Language mismatches leading to dissatisfaction



 📈 Key Results

| Metric | Language Match | No Match | Impact |
||-|-||
| Satisfaction Score | 4.5/5.0 | 3.4/5.0 | +31% ✅ |
| Resolution Time | 3.2 hours | 4.6 hours | -30% ✅ |
| First Contact Resolution | 87% | 62% | +25% ✅ |
| Ticket Volume | 210+ tickets | 5 languages | EU + Americas |

 💰 Business Impact
- €50K+ potential annual savings through optimized agent scheduling
- 15% expected CSAT increase with intelligent language routing
- 20% reduction in operational costs via faster resolution times



 🛠️ Technical Stack

- Database: PostgreSQL / SQLite
- Analysis: Python 3.11 (Pandas, NumPy, SciPy)
- Visualization: Power BI Desktop, Matplotlib, Seaborn
- Version Control: Git/GitHub
- Tools: Jupyter Notebook, VS Code


🚀 Key Insights

1. Language Matching Drives Satisfaction
Customers served in their native language rate satisfaction 31% higher (4.5 vs 3.4 out of 5.0). Statistical analysis confirms significance (p < 0.01).

2. Resolution Efficiency Gains
Language-matched tickets resolve 30% faster (3.2h vs 4.6h), reducing agent workload and improving customer experience.

3. Regional Distribution Patterns
- Europe: 97% of tickets (EN 42%, ES 18%, FR 15%, DE 12%, IT 10%)
- Americas: 3% of tickets

4. First Contact Resolution Impact
Language matching increases first-contact resolution from 62% to 87% (+25 percentage points).


💡 Business Recommendations

1. Implement Intelligent Ticket Routing
Deploy AI-based system matching customer language preferences with agent capabilities automatically.

Expected ROI: 15% CSAT increase, 20% cost reduction

2. Strategic Hiring Priorities
Focus recruitment on high-volume languages: English (42%),Spanish (18%),French (15%)

Expected Impact: 80% language match coverage

3. Language Training Investment
Prioritize training programs for agents to cover secondary languages based on ticket distribution.

4. Performance Metrics Update
Add "Language Match Rate" as core KPI for customer support team evaluation.


📁 Project Structure

multilingual-customer-support-analytics/
├── data/
│ ├── raw/ # Original 210+ ticket dataset
│ ├── processed/ # Cleaned data with language flags
│ └── data_dictionary.md # Column definitions
├── sql/
│ ├── 01_data_cleaning.sql
│ ├── 02_language_analysis.sql
│ └── 03_satisfaction_metrics.sql
├── python/
│ ├── exploratory_analysis.ipynb
│ ├── statistical_tests.py
│ └── requirements.txt
├── dashboards/
│ ├── multilingual_support_analysis.pbix
│ └── screenshots/ # Dashboard previews
├── documentation/
│ ├── methodology.md
│ └── insights_report.pdf
└── README.md



 🔧 How to Reproduce This Analysis

 Prerequisites
- Python 3.11+
- Power BI Desktop (free)
- PostgreSQL or SQLite

 Setup Instructions
1. Clone repository
git clone https://github.com/nguatta/multilingual-customer-support-analytics.git
cd multilingual-customer-support-analytics

2. Install Python dependencies
pip install -r python/requirements.txt

3. Run analysis notebook
jupyter notebook python/exploratory_analysis.ipynb

4. Open Power BI dashboard
Open dashboards/multilingual_support_analysis.pbix in Power BI Desktop




 🧩 Challenges & Solutions

 Challenge 1: Inconsistent Language Coding
Problem: Tickets used mixed formats (EN/en/English/ENG/Inglês)  
Solution: Created standardization script mapping 15+ variants to ISO 639-1 codes  
Learning: Importance of data dictionary establishment early in project lifecycle

 Challenge 2: Missing Agent Language Data
Problem: 23% of tickets lacked agent language information  
Solution: Inferred from agent_id using historical patterns (92% accuracy validation)  
Tool Used: Python fuzzy matching with `fuzzywuzzy` library

 Challenge 3: Statistical Significance Validation
Problem: Needed to prove findings weren't due to random chance  
Solution: Performed two-sample t-tests (p < 0.01) and 95% confidence intervals  
Result: Confirmed language matching effect is statistically significant



 📊 Technical Implementation Highlights

 SQL Analysis Example
 Calculate satisfaction by language match status
SELECT
CASE WHEN customer_lang = agent_lang THEN 'Matched'
ELSE 'Not Matched' END AS match_status,
AVG(satisfaction_score) AS avg_satisfaction,
AVG(resolution_hours) AS avg_resolution_time,
COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY match_status;



 Python Statistical Testing
from scipy.stats import ttest_ind

matched = df[df['lang_match'] == True]['satisfaction']
unmatched = df[df['lang_match'] == False]['satisfaction']

t_stat, p_value = ttest_ind(matched, unmatched)
print(f"Statistical significance: p-value = {p_value:.4f}")

Result: p < 0.01 (highly significant)




 👤 About This Project

Created by: Ake Marc Albert Adje  
Role: Data Analyst | Customer Experience Specialist  
Goal: Demonstrate end-to-end analytics capabilities: SQL → Python → Power BI → Business Insights

 🎓 Professional Certifications
- ✅ Google Data Analytics Professional Certificate (2025)
- ✅ IBM Data Analyst Professional Certificate (2025)
- ✅ Microsoft Power BI Data Analyst Professional Certificate (2025)

 🌐 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ake_Marc_Albert_Adje-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ake-marc-albert-adje-5b341a110)
[![Email](https://img.shields.io/badge/Email-akemarcpt@gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:akemarcpt@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_All_Projects-4285F4?style=for-the-badge)](https://datascienceportfol.io/akemarcpt)
[![GitHub](https://img.shields.io/badge/GitHub-@nguatta-181717?style=for-the-badge&logo=github)](https://github.com/nguatta)



 ⭐ Support This Project

If this analysis provided value or insights for your work, please star this repository!

💬 Questions or feedback? [Open an issue](https://github.com/nguatta/multilingual-customer-support-analytics/issues) or connect on LinkedIn.



 📜 License
This project is available under the MIT License. See LICENSE file for details.

 🔖 Keywords
`data-analytics` `power-bi` `sql` `python` `customer-support` `multilingual` `business-intelligence` `portfolio-project` `customer-satisfaction` `data-visualization`

