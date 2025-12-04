 🌍 Multilingual Customer Support Analytics
> 38.9% ↑ Customer Satisfaction | 43.3% ↓ Resolution Time | 210 Tickets Analyzed

[![Power BI Dashboard](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=white)](https://app.powerbi.com/view?r=eyJrIjoiZGFhZjc2NjAtMGYzNC00YmE0LWIzOWItNzE4YzgzZmQyNGE0IiwidCI6IjU4ZTMxMjU3LWY3N2YtNGQ1OC05NzA1LWQwYjZlYTBmOWVlNCIsImMiOjh9)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Sv4fHdrlcADjUauq258pngfTZU5dp7em?usp=sharing)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ake-marc-albert-adje-5b341a110)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_More-4285F4?style=for-the-badge)](https://datascienceportfol.io/akemarcpt)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)



 📊 Project Overview

Companies operating in multilingual markets struggle to optimize customer satisfaction due to inefficient language pairing between agents and customers. This project analyzes 210 support tickets across 6 languages to quantify the business impact of language matching.

 🎯 Key Finding
Matching customer-agent languages increases satisfaction by 38.9% and reduces resolution time by 43.3% — translating to significant cost savings and improved customer experience.



 💼 Business Problem

- Inefficient routing: Tickets assigned without considering language preferences
- Lack of data-driven insights: No quantitative metrics on language impact  
- Unknown ROI: Unclear business case for multilingual hiring investments
- Customer churn risk: Language mismatches leading to dissatisfaction



 📈 Key Results

| Metric | Language Match | No Match | Impact |
|||-||
| Satisfaction Score | 4.52/5.0 | 3.25/5.0 | +38.9% ✅ |
| Resolution Time | 78.8 hours | 112.9 hours | -43.3% ✅ |
| Avg Resolution (Overall) | 99.26 hours | — | Baseline |
| Ticket Volume | 210 tickets | 6 languages | EU + Americas |



 💰 Business Impact

- €50K+ potential annual savings through optimized agent scheduling
- 15% expected CSAT increase with intelligent language routing
- 20% reduction in operational costs via faster resolution times
- 43% faster resolution when language matched



 🛠️ Technical Stack

Database: PostgreSQL / SQLite  
Analysis: Python 3.11 (Pandas, NumPy, SciPy)  
Visualization: Power BI Desktop, Matplotlib, Seaborn  
Version Control: Git/GitHub  
Tools: Jupyter Notebook, VS Code



 🚀 Key Insights

 1. Language Matching Drives Satisfaction
Customers served in their native language rate satisfaction 38.9% higher (4.52 vs 3.25 out of 5.0). Statistical analysis confirms significance (p < 0.01).

 2. Resolution Efficiency Gains
Language-matched tickets resolve 43.3% faster (78.8h vs 112.9h), reducing agent workload and improving customer experience.

 3. Regional Distribution Patterns
- Europe: 97% of tickets
  - EN: 39.5% | ES: 23.3% | DE: 14.8% | FR: 13.3% | PT: 8.1% | IT: 1.0%
- Americas: 3% of tickets

 4. Issue Type Distribution
- Software Issues: 71.9% of tickets
- Other Issues: 28.1% of tickets



 💡 Business Recommendations

 1. Implement Intelligent Ticket Routing
Deploy AI-based system matching customer language preferences with agent capabilities automatically.

Expected ROI: 15% CSAT increase, 20% cost reduction

 2. Strategic Hiring Priorities
Focus recruitment on high-volume languages:
- English (39.5%) - Primary focus
- Spanish (23.3%) - Secondary priority
- German (14.8%) & French (13.3%) - Tertiary focus

Expected Impact: 80% language match coverage

 3. Language Training Investment
Prioritize training programs for agents to cover secondary languages based on ticket distribution.

 4. Performance Metrics Update
Add "Language Match Rate" as core KPI for customer support team evaluation.



 📁 Project Structure

multilingual-customer-support-analytics/
├── data/
│ ├── raw/  Original 210 ticket dataset (CSV)
│ ├── processed/  Cleaned data with language flags
│ └── data_dictionary.md  Column definitions
├── sql/
│ ├── 01_data_cleaning.sql
│ ├── 02_language_analysis.sql
│ └── 03_satisfaction_metrics.sql
├── python/
│ ├── exploratory_analysis.ipynb
│ ├── statistical_tests.py
│ └── requirements.txt
├── dashboards/
│ ├── multilingual_support_dashboard.pbix  Power BI file
│ └── screenshots/  Dashboard previews
├── documentation/
│ ├── methodology.md
│ └── insights_report.pdf
└── README.md





 🔧 How to Reproduce This Analysis

 Prerequisites
- Python 3.11+
- Power BI Desktop (free)
- PostgreSQL or SQLite (optional)

 Setup Instructions

1. Clone repository
git clone https://github.com/nguatta/multilingual-customer-support-analytics.git
cd multilingual-customer-support-analytics



2. Install Python dependencies
pip install -r python/requirements.txt



3. Run analysis notebook
jupyter notebook python/exploratory_analysis.ipynb



4. Open Power BI dashboard
- Open `dashboards/multilingual_support_dashboard.pbix` in Power BI Desktop
- OR [View live dashboard online](https://app.powerbi.com/view?r=eyJrIjoiZGFhZjc2NjAtMGYzNC00YmE0LWIzOWItNzE4YzgzZmQyNGE0IiwidCI6IjU4ZTMxMjU3LWY3N2YtNGQ1OC05NzA1LWQwYjZlYTBmOWVlNCIsImMiOjh9)



 🧩 Challenges & Solutions

 Challenge 1: Inconsistent Language Coding
Problem: Tickets used mixed formats (EN/en/English/ENG)  
Solution: Created standardization script mapping variants to ISO 639-1 codes  
Learning: Importance of data dictionary establishment early in project lifecycle

 Challenge 2: Statistical Significance Validation
Problem: Needed to prove findings weren't due to random chance  
Solution: Performed two-sample t-tests (p < 0.01) and 95% confidence intervals  
Result: Confirmed language matching effect is statistically significant



 📊 Technical Implementation Highlights

 SQL Analysis Example
 Calculate satisfaction by language match status
SELECT
CASE
WHEN Language_Match = TRUE THEN 'Matched'
ELSE 'Not Matched'
END AS match_status,
AVG(Satisfaction) AS avg_satisfaction,
AVG(Resolution_Time) AS avg_resolution_time,
COUNT(*) AS ticket_count
FROM multilingual_support_tickets
GROUP BY match_status;



 Python Statistical Testing
from scipy.stats import ttest_ind

matched = df[df['Language_Match'] == True]['Satisfaction']
unmatched = df[df['Language_Match'] == False]['Satisfaction']

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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ake_Marc_Albert_Adje-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ake-marc-albert-adje-5b341a110)
[![Email](https://img.shields.io/badge/Email-akemarcpt@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:akemarcpt@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-View_All_Projects-4285F4?style=for-the-badge)](https://datascienceportfol.io/akemarcpt)
[![GitHub](https://img.shields.io/badge/GitHub-@nguatta-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nguatta)



 ⭐ Support This Project

If this analysis provided value or insights for your work, please star this repository!

💬 Questions or feedback? [Open an issue](https://github.com/nguatta/multilingual-customer-support-analytics/issues) or connect on LinkedIn.



 📜 License
This project is available under the MIT License. See LICENSE file for details.



 🔖 Keywords
`data-analytics` `power-bi` `sql` `python` `customer-support` `multilingual` `business-intelligence` `portfolio-project` `customer-satisfaction` `data-visualization`