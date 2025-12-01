-- Language Distribution Analysis
-- Shows volume by customer language

SELECT DISTINCT 
    Customer_Language,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY Customer_Language
ORDER BY ticket_count DESC;

-- Expected results:
-- en (English): ~42%
-- es (Español): ~18%
-- fr (Français): ~15%
-- de (Deutsch): ~15%
-- pt (Português): ~10%

