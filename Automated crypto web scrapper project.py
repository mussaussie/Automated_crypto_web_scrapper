#!/usr/bin/env python3
"""
Cryptocurrency Web Scraper
Scrapes Bitcoin price data from CoinMarketCap and logs it to a CSV file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from datetime import datetime


def automated_call(csv_path):
    """
    Fetches current Bitcoin price from CoinMarketCap and appends to CSV.
    
    Args:
        csv_path (str): Path where the CSV file should be saved
    """
    try:
        # Fetch the webpage
        url = 'https://coinmarketcap.com/currencies/bitcoin/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        page = requests.get(url, headers=headers, timeout=10)
        page.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(page.text, 'html.parser')
        
        # Extract cryptocurrency name
        crypto_name_elem = soup.find('span', class_='sc-d1ede7e3-0 bEFegK')
        if not crypto_name_elem:
            print("Error: Could not find cryptocurrency name. Website structure may have changed.")
            return False
        
        crypto_name = crypto_name_elem.text
        crypto_name = crypto_name.replace('price', '').strip()
        
        # Extract cryptocurrency price
        crypto_price_elem = soup.find('span', class_='sc-d1ede7e3-0 fsQm base-text')
        if not crypto_price_elem:
            print("Error: Could not find cryptocurrency price. Website structure may have changed.")
            return False
        
        crypto_price = crypto_price_elem.text
        final_price = crypto_price.replace('$', '').replace(',', '').strip()
        
        # Get current timestamp
        dt = datetime.now()
        
        # Create data dictionary
        data = {
            'Crypto Name': crypto_name,
            'Price': final_price,
            'time': dt
        }
        
        # Create DataFrame
        df = pd.DataFrame([data])
        
        # Save to CSV (append if exists, create if doesn't)
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', header=False, index=False)
        else:
            df.to_csv(csv_path, index=False)
        
        print(f"[{dt.strftime('%Y-%m-%d %H:%M:%S')}] {crypto_name}: ${final_price}")
        return True
        
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """
    Main function to run the automated cryptocurrency scraper.
    """
    # Configure the CSV file path
    # UPDATE THIS PATH to your desired location
    csv_path = r'C:\Users\mussa\OneDrive\Documents\crypto_project\crypto_web_scrapper.csv'
    
    # Alternative: Use current directory
    # csv_path = 'crypto_web_scrapper.csv'
    
    # Ensure directory exists
    directory = os.path.dirname(csv_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    
    print("Starting Bitcoin price monitoring...")
    print(f"Saving data to: {csv_path}")
    print("Press Ctrl+C to stop\n")
    
    # Scraping interval in seconds
    INTERVAL = 10  # Change this to adjust frequency (recommended: 60+ for production)
    
    # Continuous scraping loop
    try:
        while True:
            success = automated_call(csv_path)
            if not success:
                print(f"Retrying in {INTERVAL} seconds...")
            time.sleep(INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\nScraping stopped by user.")
        print(f"Data saved to: {csv_path}")
    except Exception as e:
        print(f"\nFatal error: {e}")
        print(f"Data saved to: {csv_path}")


if __name__ == "__main__":
    main()
