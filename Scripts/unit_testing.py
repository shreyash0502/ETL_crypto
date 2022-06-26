from extractor import extractor
from loader import loader
from sqlalchemy import create_engine
import pymysql
from config import config
from datetime import datetime
import pandas as pd
pymysql.install_as_MySQLdb()


def unit_test_extractor():
    try:
        inp = extractor(inpdir)
    except OSError:
        print("No such file or directory exists! or the directory misses one or more of the 23 .csv files.")
    except (Exception,):
        print("Extractor isn't working fine! Debugging necessary.")
    else:
        print("Extractor is working completely fine ☻.")


def unit_test_loader():
    try:
        access_data = [datetime.now()]
        access_df = pd.DataFrame(access_data, columns=['accesstime'])
        loader(engine, 'logs', access_df, 'append')
    except (Exception,):
        print("Loader isn't working fine! Debugging necessary.")
    else:
        print("Loader is working completely fine ☻. You can check the 'logs' table to see that the current time being "
              "loaded correctly into the table. Each of these times will be available for future reference.")


print("***Welcome to unit testing module for ETL system!***")
while True:
    print("Enter yes to continue, no to exit the module.")
    ans = input()
    if ans == "no":
        print('Thank you for using ETL! Made with ♥ by Shreyash Vaish')
        break
    elif ans == "yes":
        while True:
            print("Which component you want to test? Enter 1 for extractor, 2 for loader.")
            choice = input()
            if choice.isdigit():
                choice = int(choice)
                if choice not in (1, 2):
                    print('Please enter your choice correctly!')
                    continue
                else:
                    break
            else:
                print('Please enter your choice correctly!')
                continue
        if choice == 1:
            print("Enter the input file directory(relative path only): (It must contain data for all 23 cryptos to work"
                  " properly) ")
            inpdir = input()
            unit_test_extractor()
        elif choice == 2:
            engine = create_engine(config)
            unit_test_loader()
    else:
        print('Enter your choice correctly!')
