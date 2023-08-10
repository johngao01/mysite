-- auto-generated definition
create table statistics
(
    month         int   not null
        primary key,
    total_num     int   null,
    reject        int   null,
    arrive        int   null,
    reject_rating float null,
    times         float null
);