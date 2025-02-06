# Write your MySQL query statement below
select p.project_id, round(round(coalesce(sum(e.experience_years)))/round(coalesce(count(p.project_id))),2) as average_years
from Project p 
left join Employee e
on p.employee_id = e.employee_id
group by p.project_id