CREATE TABLE IF NOT EXISTS USERS
(
    USERID integer primary key autoincrement,
    USERNAME varchar(50),
    USERPASSWORD varchar(50)
);


CREATE TABLE IF NOT EXISTS EVENTS
(
    EVENTID integer primary key autoincrement,
    EVENTNAME varchar(255),
    EVENTDESCRIPTION varchar(255),
    EVENTDATE datetime,
    USERID integer,
    FOREIGN KEY(USERID) REFERENCES USERS(USERID)
);

INSERT INTO USERS(USERNAME, USERPASSWORD)
    VALUES("Caleb Seeman", "Testing"),
    ("SJ Park", "Test"),
    ("Liam Brooke", "Tests")