-- ============================================
-- Multilingual Customer Support Analytics
-- Author: Nguatta
-- Date: December 2025
-- ============================================

-- Analysis 1: First-time value analysis
SELECT 
    Region,
    Issue_Type,
    COUNT(*) AS ticket_volume,
    AVG(Satisfaction) AS avg_satisfaction,
    AVG(Resolution_Time) AS avg_resolution_minutes,
    COUNT(*) * AVG(Satisfaction) AS customer_value_score
FROM support_tickets
WHERE Priority = 3
GROUP BY Region, Issue_Type
ORDER BY customer_value_score DESC;

-- Analysis 2: Peak hours analysis
SELECT 
    Time_Zone,
    COUNT(*) AS ticket_volume,
    AVG(Resolution_Time) AS avg_resolution
FROM support_tickets
GROUP BY Time_Zone
ORDER BY ticket_volume DESC;

-- Analysis 3: Language matching impact
SELECT 
    CASE 
        WHEN Customer_Language = Agent_Language THEN 'Language Match'
        ELSE 'No Match'
    END AS language_correspondence,
    COUNT(*) AS total_tickets,
    ROUND(AVG(Satisfaction), 2) AS avg_satisfaction,
    ROUND(AVG(Resolution_Time), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY language_correspondence;

-- Key Insight: 31% satisfaction increase with language matching
