-- afficher les noms les bases donnees li cree or liste
\l

\dt liste les tables likyin f base donnes

\q exit quit(khrj)
\c connect m3a base donnes
-- cree base donnes smiteha mydata 
create database companydb;

-- create table persons
CREATE TABLE Persons
(
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);


/*
insert into persons(firstname, lastname)
values ('kaoutar', 'depp'),('amber', 'heard');
*/
select * from persons;

delete from persons
where lastname ='depp';

select * from persons;

drop table persons;