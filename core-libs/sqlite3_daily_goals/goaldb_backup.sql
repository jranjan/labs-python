BEGIN TRANSACTION;
CREATE TABLE Goal(person_firstname TEXT, goal INT NOT NULL, desc TEXT, PRIMARY KEY(person_firstname, goal), FOREIGN KEY(person_firstname) REFERENCES Person(firstname));
INSERT INTO "Goal" VALUES('Jyoti',1,'Awake before 06:00 AM');
INSERT INTO "Goal" VALUES('Jyoti',2,'Sleep before 11:00 PM');
INSERT INTO "Goal" VALUES('Jyoti',3,'Be a listner');
INSERT INTO "Goal" VALUES('Jyoti',4,'Do not repeat yourself');
INSERT INTO "Goal" VALUES('Jyoti',5,'Eat helathy food');
INSERT INTO "Goal" VALUES('Jyoti',6,'Teach kids');
INSERT INTO "Goal" VALUES('Shivam',1,'Awake before 06:30 AM');
INSERT INTO "Goal" VALUES('Shivam',2,'Sleep before 10:30 PM');
CREATE TABLE Person(firstname TEXT PRIMARY KEY, fullname TEXT, age INT NOT NULL);
INSERT INTO "Person" VALUES('Jyoti','Jyoti Ranjan',40);
INSERT INTO "Person" VALUES('Shivam','Shivam Jyoti',9);
COMMIT;