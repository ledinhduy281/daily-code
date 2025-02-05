# Write your MySQL query statement below
-- select s.user_id, round(IFNULL(avg(c.action="confirmed"), 0) , 2) as confirmation_rate
-- from Signups s
-- left join Confirmations c
-- on s.user_id = c.user_id
-- group by s.user_id
SELECT s.user_id, 
    CASE WHEN c.user_id IS NULL THEN 0.00 
        ELSE ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*),2) END 
        AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON c.user_id = s.user_id
GROUP BY s.user_id
