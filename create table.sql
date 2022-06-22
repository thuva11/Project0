create database Bank;
use bank;
 
CREATE TABLE  Customers
(CustomerID int NOT NULL AUTO_INCREMENT,
FirstName varchar(255) NOT NULL,
LastName varchar(255) NOT NULL,
SSN int NOT NULL UNIQUE,
City varchar(255) NOT NULL,
BirthYear int NOT NULL,
PhoneNo int NOT NULL,
PRIMARY KEY (CustomerID)
);
ALTER TABLE Customers AUTO_INCREMENT=110;
 
CREATE TABLE  Login
(
Username varchar(255) NOT NULL,
Passwords varchar(255) NOT NULL,
CustomerID int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (Username),
		FOREIGN KEY (CustomerID) 
				REFERENCES Customers(CustomerID) on delete cascade
);
ALTER TABLE Login AUTO_INCREMENT=110;

 
CREATE TABLE Accounts
(
AccountNum int NOT NULL AUTO_INCREMENT,
Balance float DEFAULT 0.0,
SSN int,
PRIMARY KEY (AccountNum),
FOREIGN KEY (SSN) 
        REFERENCES Customers(SSN) on delete cascade
);
 ALTER TABLE Accounts AUTO_INCREMENT=111111111;


CREATE TABLE Transactions
(
TransID int NOT NULL AUTO_INCREMENT,
TransType varchar(255) NOT NULL,
Dates date,
Amount float not null DEFAULT 0.0,
AccountNumber int,
PRIMARY KEY (TransID),
FOREIGN KEY (AccountNumber) 
        REFERENCES Accounts(AccountNum)  on delete cascade
);

ALTER TABLE Transactions auto_increment = 5555;



