-- Multilingual Customer Support Analytics - SQL Analysis
-- Author: Ake Marc Albert Adje

-- Query 1: Language Match Impact on Satisfaction
SELECT 
    CASE 
        WHEN Language_Match = 1 THEN 'Matched'
        ELSE 'Not Matched' 
    END AS match_status,
    COUNT(*) AS ticket_count,
    ROUND(AVG(Satisfaction), 2) AS avg_satisfaction,
    ROUND(AVG(Resolution_Time), 2) AS avg_resolution_time,
    ROUND(MIN(Satisfaction), 2) AS min_satisfaction,
    ROUND(MAX(Satisfaction), 2) AS max_satisfaction
FROM multilingual_support_tickets
GROUP BY Language_Match
ORDER BY avg_satisfaction DESC;

-- Query 2: Language Distribution Analysis
SELECT 
    Customer_Language,
    COUNT(*) AS ticket_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM multilingual_support_tickets), 1) AS percentage,
    ROUND(AVG(Satisfaction), 2) AS avg_satisfaction,
    ROUND(AVG(Resolution_Time), 2) AS avg_resolution_hours
FROM multilingual_support_tickets
GROUP BY Customer_Language
ORDER BY ticket_count DESC;

-- Query 3: Regional Performance Metrics
SELECT 
    Region,
    COUNT(*) AS total_tickets,
    SUM(CASE WHEN Language_Match = 1 THEN 1 ELSE 0 END) AS matched_tickets,
    ROUND(SUM(CASE WHEN Language_Match = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS match_rate_pct,
    ROUND(AVG(Satisfaction), 2) AS avg_satisfaction,
    ROUND(AVG(Resolution_Time), 2) AS avg_resolution_time
FROM multilingual_support_tickets
GROUP BY Region;

-- Query 4: Priority vs Language Match Analysis
SELECT 
    Priority,
    COUNT(*) AS total_tickets,
    ROUND(AVG(CASE WHEN Language_Match = 1 THEN Satisfaction END), 2) AS satisfaction_matched,
    ROUND(AVG(CASE WHEN Language_Match = 0 THEN Satisfaction END), 2) AS satisfaction_unmatched,
    ROUND(AVG(CASE WHEN Language_Match = 1 THEN Resolution_Time END), 2) AS resolution_matched,
    ROUND(AVG(CASE WHEN Language_Match = 0 THEN Resolution_Time END), 2) AS resolution_unmatched
FROM multilingual_support_tickets
GROUP BY Priority
ORDER BY Priority;

-- Query 5: Business Impact Calculation
WITH language_stats AS (
    SELECT 
        CASE WHEN Language_Match = 1 THEN 'Matched' ELSE 'Unmatched' END AS status,
        AVG(Resolution_Time) AS avg_resolution,
        AVG(Satisfaction) AS avg_satisfaction,
        COUNT(*) AS ticket_count
    FROM multilingual_support_tickets
    GROUP BY Language_Match
)
SELECT 
    m.avg_resolution AS matched_resolution_hours,
    u.avg_resolution AS unmatched_resolution_hours,
    ROUND((u.avg_resolution - m.avg_resolution) / m.avg_resolution * 100, 1) AS resolution_improvement_pct,
    m.avg_satisfaction AS matched_satisfaction,
    u.avg_satisfaction AS unmatched_satisfaction,
    ROUND((m.avg_satisfaction - u.avg_satisfaction) / u.avg_satisfaction * 100, 1) AS satisfaction_improvement_pct
FROM 
    (SELECT * FROM language_stats WHERE status = 'Matched') m,
    (SELECT * FROM language_stats WHERE status = 'Unmatched') u;
