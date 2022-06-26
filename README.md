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
>
> config.py: contains the host, user and password necessary for database connection.

#### 2) SQLqueries-> This folder contains the sql queries stored in the form of .sql files. A total of 4 files whose details are described below:
>  cryptoTableCreation.sql: By running this SQL query, we can create the "cryptos" table structure which will later store all the crypo names.
>
> cryptoTableFilling.sql: This query fills up the previously created table "cryptos" with the crypto names.
>
> otherTableCreation.sql: This query is used for creating other two tables "max_price"(stores the maximum closing prices for each of the crypto over this entire period) and "growth_rates"(stores the latest annual growth rates of each of the crypto).
> 
> individualGrowthRateTablesCreation.sql: This query is used for creating the tables for storing the YOY growth rate for each of the cryptos over the entire time period of observation.

**3) Input->** This folder is the default path for all the input files, although the user can provide a separate path as well in the console application.

**4) WrongInput->** This folder is a copy of the input folder, but with some of the files missing. It has been created for demonstration purposes of unit testing.

**5) requirements.txt->** This file contains all the dependencies necessary for running the code.

**6) pretesting.bat, unit_testing.bat and table_creation.bat files->** For testing the ETL system in console environment. With the use of these batch files, I tried to automate the process of code execution in the desired order without the need to run the python files separately. Use of batch files makes the user experience much easier. Explained in detail later.



### How to run the code?

There are basically two things this code is capable of - ETL Testing which is the main operation, along with Unit-Testing which is basically the troubleshooting operation.

Before any of the operations, the first thing is to set-up the database and create the necessary tables.
For this purpose, run the table_creation.bat file(by double clicking it). The command terminal will open up which will prompt the user to enter hostname, username, and password(password will be asked twice for safety). If all the details are correct, we enter into the MySQL shell and here we can execute MySQL queries.
Note: "config.py" file gets updated automatically for storing the current user's inputs for host, user and password, when we run the table_creation.bat file.

![image](https://user-images.githubusercontent.com/56553419/175799402-60305a84-0048-495e-a27f-ea83ba9b4a9d.png)

Note: For correct execution, MySQL Server 8.0 or above must be installed and its path must be present in the system 'PATH' variable.

Once, we have entered into the MySQL shell, enter the following commands:

![image](https://user-images.githubusercontent.com/56553419/175784634-6d37e9f4-39fd-4ca4-a2fb-59818dda45f0.png)
![image](https://user-images.githubusercontent.com/56553419/175784652-c79f1042-36d7-4d51-8e57-a0bb8a051dcb.png)

By now, all these tables would be present in your database:

![image](https://user-images.githubusercontent.com/56553419/175784737-0f9b8b1f-ca21-4265-a090-00c743cb305e.png)

And the "cryptos" table will be populated. (All other tables would be populated after transformation is done!)

![image](https://user-images.githubusercontent.com/56553419/175784788-8cfd87c5-b3f1-4b61-8084-f1fd8bfc43ed.png)

After this, just do 'exit' to get out of CLI.

![image](https://user-images.githubusercontent.com/56553419/175798287-b2f51ec6-9688-464d-9758-4e0ded8f7acf.png)


Now that you have created the tables, you can begin with testing.

Firstly, create a virtual environment in the root directory.

![image](https://user-images.githubusercontent.com/56553419/175799504-4fc5c70d-a2f6-4477-a49a-314be227441f.png)
Note: Keep the name "myvenv" itself.
Now activate this virtual environment and install the dependencies.

![image](https://user-images.githubusercontent.com/56553419/175799525-d7d8d0c1-36a0-4a98-ac57-464274d4f2d0.png)

Now begin with the operations.

**The first is the ETL testing. (main operation)**
In this operation, we extract data from the 23 .csv files (Dataset) and then store the valuable information from it into the previously created tables.
Just run the pretesting.bat file(root directory).
Press any key and it will perform the testing operations(by calling driver.py file internally).

![image](https://user-images.githubusercontent.com/56553419/175798342-a765177f-b689-4151-b974-dae63bd9d535.png)
![image](https://user-images.githubusercontent.com/56553419/175798349-8010ac74-50bb-4679-b673-21c12e6de37a.png)

The pretesting has been completed and all the previous tables have been filled. You can check them in the MySQL CLI like: 

![image](https://user-images.githubusercontent.com/56553419/175798428-73287c51-9b19-4a88-aa3f-fdbb0527e03d.png)


**The second operation is unit-testing. (troubleshooting operation)**
In this operation, we check the individual components of the project and see if they are working fine.
Just run the unit_testing.bat file and follow the instructions.

### Salient features of this ETL system:
> Adding new transformations is very easy. Just need to give the user a choice, write code for transformation in a separate .py file and call that transformation based on choice, through the driver code. 
>
> Since we have separate .py file for extracting and loading the data to/from a file from/to a python variable, we can easily exchange this data with a sql database instead of a text file(using python libraries, easily accessible) if required in future.
