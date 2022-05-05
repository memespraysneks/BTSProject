CREATE TABLE USERS
(
    USERID int identity(1,1) primary key,
    USERNAME varchar(50),
    USERPASSWORD varchar(50)
);


CREATE TABLE EVENTS
(
    EVENTID int identity(1,1) primary key,
    EVENTNAME varchar(max),
    EVENTDESCRIPTION varchar(max),
    EVENTDATE datetime
);

INSERT INTO USERS(USERNAME, USERPASSWORD)
    VALUES("Caleb Seeman", "Testing"),
    ("SJ Park", "Test"),
    ("Liam Brooke", "Tests")