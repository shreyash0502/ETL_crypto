# Welcome to ETL - Made by _Shreyash Vaish_
> Extract! Transform! Load!

### How to use this ETL system?
1) For testing environment, using pretesting.bat 
2) For unit testing, use unit_testing.bat

**Note**: _All the above mentioned files are present in the root directory. These batch scripts are sufficient for testing the complete software, but if it is required to run the .py files separately(for some reason), they can be accessed in the "Scripts" subdirectory._

### What is ETL?
For an organization having large amounts of data stored in multiple databases serving the users, it is not possible for that organization to do any kind of computing on these databases, as it will slow down and deteriorate the user experience. For this purpose, any computing requires extracting the data, transforming it and loading it into a separate place. This process is known as ETL.

This project presents a small ETL setup where the data stored in the form of .csv files is loaded into memory(i.e, extracted), then some transformations are performed on this data to extract some valuable information, and finally, it is loaded into a separate MySQL database. 

**Note:** It is also possible to extract data from a database, then temperarily store into a separate database(data warehouse) while performing transformations, then finally the data can be loaded back into the database where it came from. This is what happens in an actual production environment.

The dataset being used is the "Crypocurrency Historical Prices" dataset from Kaggle.
Link to the dataset: https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory

**About the dataset:**
The dataset consists of the price history of 23 most popular cryto currencies, starting from April 28, 2013 till July 6, 2021.
The dataset contains the opening, closing, low, high prices along with transaction volumes and market cap, for every date(within the previously specified period), for each of the 23 cryptos.

We are going to extract useful information from the dataset like:
> Maximum Closing Prices
> Latest Annual Growth Rates. 
> Individual crypto currencies YOY growth rates.

All this data will be stored in the MySQL database and can be accessed anytime through the MySQL CLI.

### Structure of the project(POV: root directory):
#### 1) Scripts-> This folder contains the python code for the project.
> driver.py: This is the main code which calls different components with the data provided by the user.
>
> extractor.py: This code is used for extracting the text file from memory(from a user-given file name and directory) and loading it into a python variable.
> 
> loader.py: This code is used for loading the final output of the transformation into a text file with a user-given name and directory.
>
> 
> pretests.py: Executed by the pretesting.bat file for automatic testing purposes(explained later in detail).
> 
> unit_testing.py: Executed by the unit_testing.bat for entering into the console application for unit testing purposes(explained later in detail).

#### 2) SQLqueries-> This folder contains the sql queries stored in the form of .sql files. A total of 4 files whose details are described below:
>  cryptoTableCreation.sql: By running this SQL query, we can create the "cryptos" table structure which will later store all the crypo names.
>
> cryptoTableFilling.sql: This query fills up the previously created table "cryptos" with the crypto names.
>
> otherTableCreation.sql: This query is used for creating other two tables "max_price"(stores the maximum closing prices for each of the crypto over this entire period) and "growth_rates"(stores the latest annual growth rates of each of the crypto).
> 
> individualGrowthRateTablesCreation.sql: This query is used for creating the tables for storing the YOY growth rate for each of the cryptos over the entire time period of observation.
#### 3) Input->
> This folder is the default path for all the input files, although the user can provide a separate path as well in the console application.
#### 4) WrongInput->
> This folder is a copy of the input folder, but with some of the files missing. It has been created for demonstration purposes of unit testing.
#### 5) requirements.txt->
> This file contains all the dependencies necessary for running the code.
#### 6) pretesting.bat, unit_testing.bat and table_creation.bat files->
> For testing the ETL system in console environment. With the use of these batch files, I tried to automate the process of code execution in the desired order without the need to run the python files separately. Use of batch files makes the user experience much easier. Explained in detail later.

### For testing our ETL system, I have created two batch files:
#### 1) manual_testing.bat-> 
> By running this batch code, the user gets into the console application of the software, where he/she can follow the instructions and perform the transformations of the user given text file. 
#### 2) pretesting.bat->
> This is the automatic testing batch code. By running this batch code, the pretesting input files present in the "Input/" directory are transformed to output files stored in the "Output/" directory.
#### 3) unit_testing.bat->
> This is the batch code for unit testing, here we test the extractor, loader and the two transformations individually. Using this, we can identify which component has a bug if we make any changes in code in future. The files input/output for this code are stored in UnitTests/ directory.

### Salient features of this ETL system:
> Adding new transformations is very easy. Just need to give the user a choice, write code for transformation in a separate .py file and call that transformation based on choice, through the driver code. 
>
> Since we have separate .py file for extracting and loading the data to/from a file from/to a python variable, we can easily exchange this data with a sql database instead of a text file(using python libraries, easily accessible) if required in future.
