drop database if exists etlproject;

create database etlproject;

use etlproject;

create table cryptos (
	SNo integer NOT NULL,
	CryptoName varchar(20) NOT NULL,
    PRIMARY KEY (CryptoName));