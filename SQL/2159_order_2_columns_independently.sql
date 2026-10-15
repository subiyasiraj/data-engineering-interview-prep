select d1.first_col, d2.second_col
from (
    select first_col, row_number() over (order by first_col asc) as idx1
    from Data
) d1
join (
    select second_col, row_number() over (order by second_col desc) as idx2
    from Data
) d2
  on d1.idx1 = d2.idx2
order by d1.idx1;