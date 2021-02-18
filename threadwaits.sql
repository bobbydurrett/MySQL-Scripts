-- show the current threads and what they are waiting on

show full processlist;

use performance_schema

select * from threads;

select * from events_waits_current;


