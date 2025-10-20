# Cryptocurrency Web Scraper

A Python-based web scraper that monitors Bitcoin prices in real-time from CoinMarketCap. This automated tool fetches current Bitcoin prices every 10 seconds and logs them to a CSV file with timestamps for price tracking and analysis.

## Features

- **Real-time Bitcoin Monitoring**: Scrapes live Bitcoin price data from CoinMarketCap
- **Automated Data Collection**: Runs continuously with 10-second intervals
- **CSV Logging**: Appends new data to existing CSV file without overwriting
- **Timestamp Tracking**: Records exact date and time of each price check
- **Clean Data Processing**: Removes currency symbols and formatting for clean numeric data

## Prerequisites

- Python 3.7 or higher
- Internet connection
- pip (Python package installer)



### Running the Scraper

1. Open the script and update the CSV file path to your desired location:
```python
# Change this path to your preferred location
csv_path = r'C:\Users\YourUsername\Documents\crypto_project\crypto_web_scrapper.csv'
```

2. Run the script:
```bash
python crypto_scraper.py
```

3. The script will start collecting Bitcoin prices every 10 seconds and display output in the console.

4. To stop the scraper, press `Ctrl + C` (or `Cmd + C` on Mac).

### Configuration

Modify the scraping interval by changing the `time.sleep()` value in the script:

```python
while True: 
    automated_call()
    time.sleep(10)  # Change to desired interval in seconds
```

**Recommended intervals:**
- Testing: `10` seconds
- Development: `60` seconds (1 minute)
- Production: `300` seconds (5 minutes) or higher

## How It Works

The scraper follows this workflow:

1. **Fetch Page**: Sends HTTP GET request to CoinMarketCap's Bitcoin page
2. **Parse HTML**: Uses BeautifulSoup to parse the webpage content
3. **Extract Data**: Locates Bitcoin name and price using CSS class selectors
4. **Clean Data**: Removes "$" symbol and "price" text from extracted data
5. **Add Timestamp**: Records current date and time
6. **Save to CSV**: Appends new row to CSV file (creates file if doesn't exist)
7. **Repeat**: Waits 10 seconds and repeats the process

## Output Format

The generated CSV file (`crypto_web_scrapper.csv`) contains three columns:

| Crypto Name | Price | time |
|-------------|-------|------|
| Bitcoin | 45123.45 | 2025-10-20 14:30:15.123456 |
| Bitcoin | 45125.30 | 2025-10-20 14:30:25.234567 |
| Bitcoin | 45120.80 | 2025-10-20 14:30:35.345678 |

## Code Overview

### Main Function: `automated_call()`

```python
def automated_call():
    # Fetches Bitcoin data and appends to CSV
    # Handles both new file creation and appending to existing file
```

**Key Components:**
- URL targeting: `https://coinmarketcap.com/currencies/bitcoin/`
- CSS selectors for scraping:
  - Name: `span.sc-d1ede7e3-0.bEFegK`
  - Price: `span.sc-d1ede7e3-0.fsQm.base-text`
- Data cleaning: Removes "$" and "price" text
- CSV handling: Smart append mode to preserve historical data

## Important Notes

### ⚠️ Legal and Ethical Considerations

- **Web Scraping Legality**: Review CoinMarketCap's [Terms of Service](https://coinmarketcap.com/terms/) before using
- **Rate Limiting**: The default 10-second interval is aggressive. Consider increasing to 60+ seconds
- **Official API**: For production use, consider [CoinMarketCap's official API](https://coinmarketcap.com/api/)
- **Respectful Scraping**: Avoid overloading servers with excessive requests

### 🐛 Potential Issues

**CSS Class Changes**: CoinMarketCap may update their website design, breaking the CSS selectors. If scraping fails:
1. Inspect the Bitcoin page in your browser
2. Find the new CSS classes for name and price elements
3. Update the class names in the script

**Example Fix:**
```python
# Old (may break)
crypto_name = soup.find('span', class_='sc-d1ede7e3-0 bEFegK').text

# Update with new classes when website changes
crypto_name = soup.find('span', class_='NEW-CLASS-HERE').text
```

## Troubleshooting

### Common Issues

**Problem**: Script crashes with `AttributeError: 'NoneType' object has no attribute 'text'`
- **Cause**: CSS selectors are outdated or page structure changed
- **Solution**: Inspect the webpage and update the CSS class names

**Problem**: CSV file not found or permission denied
- **Cause**: Invalid file path or insufficient permissions
- **Solution**: Update the file path and ensure the directory exists

**Problem**: No data appearing in CSV
- **Cause**: Script may not have write permissions
- **Solution**: Check folder permissions or change output directory

**Problem**: `ConnectionError` or timeout
- **Cause**: Network issues or CoinMarketCap is unreachable
- **Solution**: Check internet connection, try again later, or add error handling

## Improvements & Future Enhancements

Suggested improvements for contributors:

- [ ] Add error handling for network failures and parsing errors
- [ ] Implement retry logic with exponential backoff
- [ ] Add command-line arguments for configuration (interval, output path)
- [ ] Support multiple cryptocurrencies
- [ ] Add logging system instead of CSV-only output
- [ ] Create data visualization dashboard
- [ ] Add price alert notifications (email/SMS)
- [ ] Use CoinMarketCap's official API for reliability
- [ ] Add database storage option (SQLite/PostgreSQL)
- [ ] Implement graceful shutdown handling
- [ ] Add unit tests
- [ ] Create Docker container for easy deployment



## Disclaimer

**This tool is for educational purposes only.** 

- Price data accuracy is not guaranteed
- Web scraping may violate website terms of service
- Not intended for financial decision-making
- Always verify data through official sources
- Use at your own risk

## Acknowledgments

- Data source: [CoinMarketCap](https://coinmarketcap.com/)
- Built with Python, Requests, BeautifulSoup, and Pandas

## Contact & Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section above

---

**⚡ Quick Tip**: For more stable and reliable data access, consider using CoinMarketCap's official API instead of web scraping.
