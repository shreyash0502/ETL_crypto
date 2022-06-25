from driver import driver

print('****Welcome to ETL!****')

print('Here, we are going to extract the "CryptoCurrency Historical Prices" dataset into our program and then, we will '
      'extract useful information from it like Maximum Closing Prices, Latest Annual Growth Rates. We will also check '
      'the individual crypto currencies for their YOY growth rates.')

print('-----------------------------------------------------')

print('This information(besides many other factors) can prove to be really helpful while making the choice of where and'
      ' how much to invest in different cryptos.')

print('-----------------------------------------------------')

print('About the Dataset: "CryptoCurrency Historical Prices" dataset.')
print('The dataset consists of the price history of 23 most popular cryto currencies, starting from April 28, 2013 till'
      ' July 6, 2021.')
print('The dataset contains the opening, closing, low, high prices along with transaction volumes and market cap, for '
      'every date(within the previously specified period), for each of the 23 cryptos.')

driver('Input')

print("All the pretests have been completed and saved into the database. You can check them using MySQL command line!")
print("Thank you for using ETL! Made with ♥ by Shreyash Vaish")
