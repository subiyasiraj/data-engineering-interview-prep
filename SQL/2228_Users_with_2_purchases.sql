with cte as (
select *, lead(purchase_date) over(partition by user_id order by purchase_date asc) as next_purchase_date
  from purchases
)
select user_id
from cte
where next_purchase_date - purchase_date <= 7
group by user_id
order by user_id