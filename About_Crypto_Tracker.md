This Python script interacts with the CoinMarketCap API to retrieve and display detailed information about various cryptocurrencies. The main functionalities of the script include fetching a list of all cryptocurrencies, finding a specific cryptocurrency by name, retrieving its social media handles and contract information, and displaying its financial statistics.

### Code Overview:

1. **Class Definition (`CoinMarketCap`)**:

   - **Initialization (`__init__`)**: Sets up the API key and request headers for accessing the CoinMarketCap API.
   - **Fetching All Cryptocurrencies (`get_all_crypto_currencies`)**: Sends a request to the API to retrieve a list of all cryptocurrencies and handles potential errors.
   - **Finding Cryptocurrency ID (`find_crypto_currency_id`)**: Searches for a specific cryptocurrency by its name in the list of all cryptocurrencies and returns its ID.
   - **Fetching Social Media and Contract Info (`get_social_media_handles_of_crypto`)**: Retrieves social media handles and contract information for a specific cryptocurrency using its ID and handles potential errors.
   - **Fetching Financial Statistics (`financial_statistics_of_crypto`)**: Retrieves financial data, such as price, market cap, volume, and supply details for a specific cryptocurrency using its ID and handles potential errors.
   - **Displaying Data (`display_crypto_currency_data`)**: Prints the retrieved information in a readable format.

2. **Main Execution Block**:

   - Creates an instance of the `CoinMarketCap` class.
   - Prompts the user to input the name of a cryptocurrency.
   - Fetches the list of all cryptocurrencies.
   - Finds the ID of the specified cryptocurrency.
   - Retrieves and displays the social media handles, contract info, and financial statistics for the specified cryptocurrency.

### Key Functionalities:

- **Fetching Data**: The script uses the CoinMarketCap API to fetch various data points about cryptocurrencies, including their names, IDs, social media links, contract addresses, prices, market caps, and supply details.
- **Error Handling**: The script includes basic error handling to manage API request failures and missing data gracefully.
- **User Interaction**: The script prompts the user to input a cryptocurrency name, making it interactive and user-friendly.

This code is useful for anyone looking to track detailed information about cryptocurrencies, providing a comprehensive snapshot of both market statistics and social media presence.