# Write your MySQL query statement below
-- select name
-- from Employee
-- where id in (
--     select managerId
--     from Employee
--     group by managerId
--     having count(*) >= 5
-- )
select b.name from Employee b join Employee a on b.id = a.managerId group by b.id having count(*) >= 5

