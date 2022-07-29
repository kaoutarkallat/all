create database Customer;
create table Customer
(
    FirstName varchar(50),
    LastName varchar(50),
    Age int     
);
insert into Customer(FirstName, LastName, Age)
values ('joy', 'blue', 40);

insert into Customer(FirstName, LastName, Age)
values ('alex', 'john', 40);

insert into Customer(FirstName, LastName, Age)
values ('sekandr', 'jol', 40);

insert into Customer(FirstName, LastName, Age)
values ('kaoutar', 'kalla', 40);

select * from Customer;


select * from Customer
where FirstName = 'alex'and LastName = 'john';

delete from Customer
where FirstName = 'alex'
and LastName like 'john';


update Customer
set Age = 22
where FirstName = 'kaoutar'
and LastName = 'kalla';



alter table customer
add City varchar(50);

update Customer 
set City = 'NewYork';

update Customer
set City= 'spain' 
where FirstName = 'kaoutar'
and LastName = 'kalla';


create table customer2
(
    ID serial,
    FirstName varchar(50),
    LastName varchar(50),
    Age int,
    City varchar(50)

);

alter table customer2
add price float;

alter table customer2
add birthday date;

insert into customer2(FirstName, LastName, Age, City, price, birthday)
values('maram', 'bend', 3, 'morocco', 5.95, '2000-12-16');


delete from customer2
where ID = 1;




insert into persons(ID, FirstName, Age)
values(1, 'kaou', 21)


create table persons2(
    ID int not null, 
    FirstName varchar(255) not null,
    LastName varchar(255),
    Age int,
    profession varchar(255)
);
drop table persons1;
insert into persons1(ID, FirstName,LastName, Age)
values(9, 'israe', 'bend' ,21);

create index myindex on persons1(FirstName);


alter table persons1
add primary key (ID);\



CREATE TABLE Orders(
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY(OrderID),
    FOREIGN KEY(PersonID)REFERENCES Persons1(ID)
);

insert into Orders(OrderID, OrderNumber, PersonID)
values(1, 45644, 8);



select FirstName as fn, LastName as ln, Age from persons1;
select FirstName, LastName, Age from persons1;
select FirstName, LastName, Age, FirstName || ' ' || LastName as fullname  from persons1;

select * from persons1;

select FirstName, LastName, OrderNumber from persons1
join Orders;


insert into persons1(ID, FirstName, LastName, Age)
values (1,'Angelina', 'Julie', 45),
        (2,'Brad', 'Pitt', 56),
        (3,'George', 'Cloony', 61),
        (4,'Jennifer','Annistan',51)
        ;
insert into persons2(ID, FirstName, LastName, Age, profession)
values (5,'Taylor', 'Swift', 55, 'singer'),
        (6,'Elon', 'Musk', 56, 'entrepreneur'),
        (7,'Chris', 'Rock', 33, 'comedian'),
        (8,'Conan','Obrian',51, 'show hoster')
        ;

select ID, FirstName, LastName, Age from persons1
union
select ID, FirstName, LastName, Age from persons2;

create table bank_account(
    ID serial,
    personID int not null, 
    balance real
);

insert into bank_account(personID, balance)
values  (7, 33.8),
        (6, 56999.7),
        (5, 558.7),
        (8,5187.5)
        ;
drop table bank_account;

select * from Persons1 full outer join bank_account
on persons1.ID = bank_account.personID;



select FirstName, LastName, age, 'Morocco' as country from persons1;le

create table freelancers(
    ID serial,
    name varchar(255),
    project varchar(255),
    price real,
    gender varchar(255)
);

insert into freelancers(name, project, price, gender)
values
('hassan', 'web developpement', 400,'male'),
('kaoutar', 'python app', 600, 'female'),
('cristiano', 'trading', 700,'male'),
('cristiano', 'scraping', 900,'male'),
('cristiano', 'banking', 500,'male'),
('kaoutar', 'banking', 2300,'female');


select 
    sum(price), 
    count(project) as nombre,
    sum(price)/ count(project) as moyenne,
    avg(price),
    gender
into tab1
from freelancers 
group by gender
having sum(price) >=2000;

create table persons3(
    ID serial,
    FirstName varchar(255),
    LastName varchar(255),
    Age int

);
select id, FirstName into persins3 from persons1;

drop database testdb;


create table copypersons1 as
select * from persons1;

alter table persons1
add employed boolean;

alter table persons1
drop employed;

alter table persons1
alter column employed type varchar(255);

alter table persons1
rename employed to emp;

alter table persons1
add unique (ID);
insert into persons1(ID, FirstName, LastName, age)
values(11, 'james','bond',49);

insert into persons1(id, FirstName, LastName, Age, emp )
values(19, 'chris', 'brown', 52, 'chomeur');

alter table persons1
add unique (FirstName);

alter table persons1
drop constraint persons1_id_firstname_key;

alter table persons1
add constraint check_age check(age>10);

alter table persons1
drop constraint check_age;

alter table persons1
alter column emp set default 'unemployed';


alter table persons1
add column birthday date;

update persons1
set birthday = '2000-12-16';


update persons1
set birthday = '2008-02-21' where FirstName = 'israe';