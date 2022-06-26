create table max_price (
	CryptoName varchar(20) NOT NULL,
	MaxClose double,
	PRIMARY KEY (CryptoName));
    
create table growth_rates (
	CryptoName varchar(20) NOT NULL,
	growthRate double,
	PRIMARY KEY (CryptoName));
    
