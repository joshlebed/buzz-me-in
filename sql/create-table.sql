create table passcodes(
    passcode varchar(15),
    startTime timestamptz,
    endTime timestamptz,
    id serial primary key
);
insert into passcodes(passcode, startTime, endTime)
values (
        'letmein',
        '2022-02-04 00:00:00-05',
        '2023-02-04 00:00:00-05'
    );