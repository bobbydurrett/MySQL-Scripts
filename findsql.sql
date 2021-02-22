use sys

-- find a query that fits a pattern
-- and was used in a time range
-- example looks for a LOCK command affecting MY_TABLE

select * 
from x$statement_analysis
where
query like 'LOCK%MY_TABLE%' 
and first_seen <= str_to_date('2021-02-15 16:30','%Y-%m-%d %H:%i')
and last_seen >= str_to_date('2021-02-15 16:45','%Y-%m-%d %H:%i');
