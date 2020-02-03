DROP DATABASE if exists wisconsinbenchmark;
CREATE DATABASE wisconsinbenchmark owner postgres;
\connect wisconsinbenchmark

DROP TABLE if exists HUNDREDKTUP;

CREATE TABLE HUNDREDKTUP (
    unique1 int NOT NULL,
    unique2 int PRIMARY KEY NOT NULL,
    two int NOT NULL,
    four int NOT NULL,
    ten int NOT NULL,
    twenty int NOT NULL,
    onePercent int NOT NULL,
    tenPercent int NOT NULL,
    twentyPercent int NOT NULL,
    fiftyPercent int NOT NULL,
    unique3 int NOT NULL,
    evenOnePercent int NOT NULL,
    oddOnePercent int NOT NULL,
    stringu1 varchar(52) NOT NULL,
    stringu2 varchar(52) NOT NULL,
    string4 varchar(52) NOT NULL,
)

ALTER TABLE HUNDREDKTUP OWNER to postgres