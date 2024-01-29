create database Hospital;
use hospital;


create table docinfo(
did int primary key,
dfname varchar(20) NOT NULL ,
dlname varchar(20) NOT NULL,
dsex enum('Male','Female'),
dexp int  NOT NULL,
ddept varchar(20) NOT NULL,
dqual varchar(30) NOT NULL,
dphn int NOT NULL unique,
demail varchar(30) unique,
shift varchar(30) NOT NULL,
check (dphn between 9800000000 and 9899999999),
check (dexp between 0 and 60),
check (demail like '%@gmail.com'),
check (shift like '__:__ to __:__')
);

create table patientinfo(
pid int primary key auto_increment,
pfname varchar(20) NOT NULL,
plname varchar(20) NOT NULL,
psex enum('Male','Female'),
paage int  NOT NULL,
paddress varchar(30) NOT NULL,
pemail varchar(30) ,
pphn bigint NOT NULL,
check (paage between 0 and 120),
check (pphn between 9800000000 and 9899999999),
check (pemail like '%@gmail.com')
);


create table appointmentdetails(
aid int primary key ,
adate date not null,
atime time not null,
did int not null,
check (aid>9999),
foreign key (did) references docinfo (did)
);

create table appointmentSetup(
turn int not null ,
pid int primary key,
status enum('Visited','Not Visited') default "Not Visited",
foreign key (pid) references patientinfo (pid),
aid int ,
foreign key (aid) references appointmentdetails (aid)
);

create table prep(
pid int primary key ,
height float not null,
weight float not null,
bp varchar(7) not null,
sugar int,
cholestrol int,
diagnosis varchar(30) not null,
prescription varchar(500),
foreign key (pid) references appointmentSetup(pid),
check (bp like '___/___')
);

create table paymentinfo(
opdcost float not null default 750,  
labcost float,
medicinecost float,
miscellaneous float,
pid int primary key ,
foreign key (pid) references appointmentSetup(pid)
);


create view patient_report as
select P.pfname as First_Name,P.plname as Last_Name,P.paage as Age, 
P.psex as Sex, R.height as Height, R.weight as Weight, R.bp as BP,
R.sugar as Sugar,R.cholestrol as Cholestrol,R.diagnosis as Diagnosis,R.prescription as Prescription
from patientinfo as P natural join prep as R;



create view bill as
select P.pfname as First_Name,P.plname as Last_Name,A.opdcost as OPD_Cost, 
A.labcost as Lab_Cost, A.medicinecost as Medicine_cost, 
A.miscellaneous as Miscellaneous_Cost, 
sum(A.labcost)+sum(A.medicinecost)+sum(A.miscellaneous)+sum(A.opdcost) as Total_Cost
from patientinfo as P natural join paymentinfo as A;

select * from patientinfo;
insert into patientinfo(pfname,plname,psex,paage,paddress,pemail,pphn)
values ('Srijana','Bhatta','Female',55,'Kanchanpur','srijana@gmail.com',9875874864);
insert into paymentinfo
values (50,100,20,10,5,1);

SELECT Total_Cost,First_Name
FROM bill;