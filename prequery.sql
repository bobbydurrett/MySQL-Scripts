-- run this before the query that you are trying to tune

use MYDB;

drop table beforetables;

create table beforetables as
select * from sys.x$schema_table_statistics;

drop table beforeindexes;

create table beforeindexes as
select * from sys.x$schema_index_statistics;
