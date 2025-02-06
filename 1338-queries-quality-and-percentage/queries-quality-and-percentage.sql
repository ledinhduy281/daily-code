# Write your MySQL query statement below
-- select query_name, round(avg(sum(rating)/sum(position)),2) as quality, (select round(count(rating)/count(query_name)*100,2) from Queries where rating < 3) as poor_query_percentage
-- from Queries q
-- group by query_name

# Write your MySQL query statement below
SELECT query_name, 
       ROUND(avg(rating / position), 2) AS quality, 
       ROUND((sum(rating < 3)/count(*))*100,2) AS poor_query_percentage
FROM Queries q
GROUP BY query_name;
