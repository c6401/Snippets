!pip3 install --user ipython-sql
%load_ext sql

%%sql postgresql://...:...@localhost/db
select * from ...
