use sys

select * from statement_analysis where digest = 'c97302f3fe1415211816e99fc9b69165';

select * from x$statement_analysis where digest = 'c97302f3fe1415211816e99fc9b69165';

use performance_schema

select * from events_statements_summary_by_digest where digest = 'c97302f3fe1415211816e99fc9b69165';


