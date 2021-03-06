CREATE TABLE IF NOT EXISTS USERS
(
    USERID integer primary key auto_increment,
    USERNAME varchar(50) UNIQUE,
    USERPASSWORD varchar(1000),
    USEREMAIL varchar(100)
);


CREATE TABLE IF NOT EXISTS EVENTS
(
    EVENTID integer primary key auto_increment,
    EVENTNAME varchar(255),
    EVENTDESCRIPTION varchar(255),
    EVENTDATE datetime,
    USERID integer,
    FOREIGN KEY(USERID) REFERENCES USERS(USERID)
);

