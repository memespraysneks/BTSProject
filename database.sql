CREATE TABLE USERS
(
    USERID varchar(10) primary key,
    USERNAME varchar(50),
    USERPASSWORD varchar(50)
);


CREATE TABLE EVENTS
(
    EVENTID varchar(10) primary key,
    EVENTNAME varchar(50),
    EVENTDATE datetime
);

INSERT INTO USERS
    VALUES("USER001", "Caleb Seeman", "Testing"),
    ("USER002", "SJ Park", "Test"),
    ("USER003", "Liam Brooke", "Tests")