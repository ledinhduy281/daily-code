# Write your MySQL query statement below
with cte1 as (
    select visited_on, sum(amount) as sum_amount
from customer
group by visited_on
order by visited_on
),
    cte2 as (
    select cte1.visited_on,
        sum(cte1.sum_amount) over (order by cte1.visited_on rows between 6 preceding and current row) as amount,
        lag(cte1.visited_on, 6) over() as day
    from cte1
)
select cte2.visited_on, cte2.amount, round((cte2.amount/7),2) as average_amount
from cte2
where day is not null