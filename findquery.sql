use sys

-- find a query that fits a pattern
-- and was used in a time range

select * 
from statement_analysis
where
query like 'LOCK%' 
and first_seen <= str_to_date('2021-02-15 16:30','%Y-%m-%d %H:%i')
and last_seen >= str_to_date('2021-02-15 16:45','%Y-%m-%d %H:%i');
