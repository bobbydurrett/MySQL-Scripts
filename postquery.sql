-- run this after the query that you are trying to tune
-- produces a report of overall system activity

use MYDB;

select 
a.table_schema,
a.table_name,
(a.total_latency - IFNULL(b.total_latency, 0))/1000000000000 total_latency_seconds,
(a.rows_fetched - IFNULL(b.rows_fetched, 0)) rows_fetched,
(a.fetch_latency - IFNULL(b.fetch_latency, 0))/1000000000000 fetch_latency_seconds,
(a.rows_inserted - IFNULL(b.rows_inserted, 0)) rows_inserted,
(a.insert_latency - IFNULL(b.insert_latency, 0))/1000000000000 insert_latency_seconds,
(a.rows_updated - IFNULL(b.rows_updated, 0)) rows_updated,
(a.update_latency - IFNULL(b.update_latency, 0))/1000000000000 update_latency_seconds,
(a.rows_deleted - IFNULL(b.rows_deleted, 0)) rows_deleted,
(a.delete_latency - IFNULL(b.delete_latency, 0))/1000000000000 delete_latency_seconds,
(a.io_read_requests - IFNULL(b.io_read_requests, 0)) io_read_requests,
(a.io_read - IFNULL(b.io_read, 0)) io_read,
(a.io_read_latency - IFNULL(b.io_read_latency, 0))/1000000000000 io_read_latency_seconds,
(a.io_write_requests - IFNULL(b.io_write_requests, 0)) io_write_requests,
(a.io_write - IFNULL(b.io_write, 0)) io_write,
(a.io_write_latency - IFNULL(b.io_write_latency, 0))/1000000000000 io_write_latency_seconds,
(a.io_misc_requests - IFNULL(b.io_misc_requests, 0)) io_misc_requests,
(a.io_misc_latency - IFNULL(b.io_misc_latency, 0))/1000000000000 io_misc_latency_seconds
from
sys.x$schema_table_statistics a
left join
beforetables b
on
a.table_schema = b.table_schema and
a.table_name = b.table_name
where
(a.total_latency - IFNULL(b.total_latency, 0))/1000000000000 > 0
order by total_latency_seconds desc;

select 
a.table_schema,
a.table_name,
a.index_name,
(a.rows_selected - IFNULL(b.rows_selected, 0)) rows_selected,
(a.select_latency - IFNULL(b.select_latency, 0))/1000000000000 select_latency_seconds,
(a.rows_inserted - IFNULL(b.rows_inserted, 0)) rows_inserted,
(a.insert_latency - IFNULL(b.insert_latency, 0))/1000000000000 insert_latency_seconds,
(a.rows_updated - IFNULL(b.rows_updated, 0)) rows_updated,
(a.update_latency - IFNULL(b.update_latency, 0))/1000000000000 update_latency_seconds,
(a.rows_deleted - IFNULL(b.rows_deleted, 0)) rows_deleted,
(a.delete_latency - IFNULL(b.delete_latency, 0))/1000000000000 delete_latency_seconds
from
sys.x$schema_index_statistics a
left join
beforeindexes b
on
a.table_schema = b.table_schema and
a.table_name = b.table_name and
a.index_name = b.index_name
where
(a.select_latency - IFNULL(b.select_latency, 0))/1000000000000 > 0
order by select_latency_seconds desc;

drop table beforetables;

drop table beforeindexes;
