# Welcome to ETL - Made by _Shreyash Vaish_ with ❤️
> Extract! Transform! Load!

### How to use this ETL system?
1) As a console application, by running manual_testing.bat
2) For seeing the pretests, using pretesting.bat 
3) For unit testing, use unit_testing.bat

**Note**: _All the above mentioned files are present in the root directory. These batch scripts are sufficient for testing the complete software, but if it is required to run the .py files separately, run them from the root directory itself (although they are present in the "Scripts/" directory). Otherwise, it might result in "file not found" error._

### What is ETL?
For an organization having large amounts of data stored in multiple databases serving the users, it is not possible for that organization to do any kind of computing on these databases, as it will slow down and deteriorate the user experience. For this purpose, any computing requires extracting the data, transforming it and loading it into a separate place. This process is known as ETL.

This project presents a small ETL setup where the data stored in a text file in memory is extracted, some transformation is performed on this data and then it is loaded to a separate text file. 

### The following transformations have been included in our setup:
> Capitalizing the text.
>
> Counting number of unique words, using space as separator.

### Different components of the ETL system:
#### 1) Scripts->
> driver.py: This is the main code which calls different components with the data provided by the user.
>
> extractor.py: This code is used for extracting the text file from memory(from a user-given file name and directory) and loading it into a python variable.
> 
> loader.py: This code is used for loading the final output of the transformation into a text file with a user-given name and directory.
> 
> trans1.py: Contains the code for first transformation.
> 
> trans2.py: Contains the code for second transformation.
> 
> pretests.py: Executed by the pretesting.bat file for automatic testing purposes(explained later in detail).
> 
> testing.py: Executed by the manual_testing.bat for entering into the console application for manual testing purposes(explained later in detail).

#### 2) Input->
> This folder is the default path for all the input files, although the user can provide a separate path as well in the console application.
#### 3) Output->
> This folder is the default path for all the output files, although the user can provide a separate path as well in the console application.
#### 4) UnitTests->
> This folder contains and stores the input/output files required for unit testing.
#### 5) manual_testing.bat, pretesting.bat and unit_testing.bat files->
> For testing the ETL system. Explained in detail later.

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