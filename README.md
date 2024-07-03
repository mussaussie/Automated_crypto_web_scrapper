Project Title: Cryptocurrency Web Scraper

Description:
This Python script scrapes real-time cryptocurrency data from CoinMarketCap using BeautifulSoup and requests. It extracts the name, price, and timestamp of a specific cryptocurrency (e.g., Bitcoin) and stores the data in a CSV file. The automated_call function automates data retrieval at intervals, useful for real-time price monitoring.

Features:

Web Scraping: Utilizes BeautifulSoup for parsing HTML and requests for fetching web pages.
Data Handling: Stores cryptocurrency name, price, and timestamp in a pandas DataFrame and exports it to CSV.
Automation: Implements a continuous scraping mechanism using a while loop with a time delay.
Dependencies:

pandas
requests
BeautifulSoup
Usage:

Setup: Install required libraries (pip install pandas requests beautifulsoup4).
Execution: Run the script to start scraping cryptocurrency data from CoinMarketCap.
Output: Check the generated CSV file (crypto_web_scrapper.csv) for the latest data updates.
Contributing:
Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues for suggestions and improvements, such as adding support for multiple cryptocurrencies or enhancing error handling.

License:
This project is licensed under the MIT License - see the LICENSE file for detail
