
import requests
import json

class CoinMarketCap:

  apikey = "8dfd8992-3ef5-4fa7-8c09-0931fe2b7a8d"
  baseURL = "https://pro-api.coinmarketcap.com/v1/"

       
# Initialize headers with API key
  def __init__(self):
      
      self.header = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CoinMarketCap.apikey,
      }

# Fetch the list of all cryptocurrencies
  def get_all_crypto_currencies(self):

      try:
         self.url = CoinMarketCap.baseURL + 'cryptocurrency/map'
         self.response = requests.get(self.url, headers=self.header)
         self.cryptosList = json.loads(self.response.text)
         return self.cryptosList

      except: print(f"\n>> Error fetching cryptocurrency")
   

# Find the ID of the cryptocurrency by its name
  def find_crypto_currency_id(self, listOfAllCryptoCurrencies, cryptoName):
     
    if listOfAllCryptoCurrencies:

      for self.cryptoName in listOfAllCryptoCurrencies['data']:
        
            if cryptoName == self.cryptoName['name'].lower():
               return self.cryptoName['id']
        
      else:
           print("\n>> No crypto currency found")
           return None
      
      
# Fetch social media handles and contract info of the cryptocurrency by its ID        
  def get_social_media_handles_of_crypto(self, cryptoID):

    self.parameter = { 'id' : cryptoID }

    if cryptoID:

      try:
         self.url = CoinMarketCap.baseURL + 'cryptocurrency/info'
         self.response = requests.get(self.url, params=self.parameter, headers=self.header)
         self.cryptoSocialInfo = json.loads(self.response.text)
   
         self.socialLinks = self.cryptoSocialInfo['data'][str(cryptoID)]['urls']
         self.contractAddress = self.cryptoSocialInfo['data'][str(cryptoID)]['contract_address'][0]
         self.contractName = self.contractAddress['platform']

      except : print(f"\n>> Error fetching  contract information")

   
# Fetch financial statistics of the cryptocurrency by its ID
  def financial_statistics_of_crypto(self, cryptoID):
     
    self.parameter = { 'id' : cryptoID }

    if cryptoID:
      
      try:
         self.url = CoinMarketCap.baseURL + 'cryptocurrency/quotes/latest'
         self.response = requests.get(self.url, params=self.parameter, headers=self.header)
         self.financialStatistics = json.loads(self.response.text)

         self.financialData = self.financialStatistics['data'][str(cryptoID)]
         self.marketData = self.financialData['quote']['USD']
       
      except: print(f"\n>> Error fetching financial statistics")


# Display the fetched data of the cryptocurrency
  def display_crypto_currency_data(self, cryptoName):
     
   if self.cryptoSocialInfo or self.financialStatistics:

     try:
        
      print(f"\n-----------Basic Information of {cryptoName.title()}-----------\n")
      print(f">> Name : {self.financialData['name']}")
      print(f">> ID : {self.financialData['id']}")
      print(f">> Symbol : {self.financialData['symbol']}")
      print(f">> Rank : {self.financialData['cmc_rank']}")

      print(f"\n-----------Market Statistics of {cryptoName.title()}-----------\n")
      print(f">> Price(USD) : ${self.marketData['price']}")
      print(f">> 1 hour percent change : {self.marketData['percent_change_24h']}%")
      print(f">> Market Capital(USD) : ${self.marketData['market_cap']}")
      print(f">> Volume(24h)(USD) : ${self.marketData['volume_24h']}")
      print(f">> Volume/Market Cap(24h): {self.marketData['volume_24h'] / self.marketData['market_cap']}%")
      print(f">> Circulating Supply : {self.financialData['circulating_supply']} {cryptoName.title()}")
      print(f">> Total Supply : {self.financialData['total_supply']} {cryptoName.title()}")
      print(f">> Fully diluted market cap(USD) : ${self.marketData['fully_diluted_market_cap']}")

      print(f"\n-----------Social Media Handles and Contracts of {cryptoName.title()}-----------\n")
      print(f">> Website : {str(self.socialLinks.get('website'))[2:-2]}")
      print(f">> Technical Document: {str(self.socialLinks.get('technical_doc'))[2:-2]}")
      print(f">> Twitter: {str(self.socialLinks.get('twitter'))[2:-2]}")
      print(f">> Reddit: {str(self.socialLinks.get('reddit'))[2:-2]}")
      print(f">> Message Board: {str(self.socialLinks.get('message_board'))[2:-2]}")
      print(f">> Chat: {str(self.socialLinks.get('chat'))[2:-2]}")
      print(f">> Contract Address : {self.contractAddress.get('contract_address')}") 
      print(f">> Contract Name : {self.contractName.get('name')}\n")
   
     except : print(f"\n>> No more data available\n")


if __name__ == "__main__":
  
   # Create an instance of CoinMarketCap
   coinMarketCap = CoinMarketCap()

   print("\n----WELCOME TO THE `CRYPTO TRACKER!` HERE YOU CAN GET ALL DATA ABOUT THE VARIOUS `CRYPTO CURRENCIES`----\n")

   # Get the cryptocurrency name from the user
   cryptoName = input(">> Enter crypto currency name : ")


   try:
   
    # Fetch the list of all cryptocurrencies
    listOfAllCryptoCurrencies = coinMarketCap.get_all_crypto_currencies()
 
    # Find the ID of the cryptocurrency
    cryptoID = coinMarketCap.find_crypto_currency_id(listOfAllCryptoCurrencies, cryptoName.lower())
  
    # Fetch social financial statistics of the cryptocurrency
    coinMarketCap.financial_statistics_of_crypto(cryptoID)

    # Fetch social media handles of the cryptocurrency
    coinMarketCap.get_social_media_handles_of_crypto(cryptoID)
 
    # Display the fetched data
    coinMarketCap.display_crypto_currency_data(cryptoName)
 
   except:
      print("Enter the valid crypto name")
