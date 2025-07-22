#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
import pytz
import re

# Sri Lanka timezone
sri_lanka_tz = pytz.timezone("Asia/Colombo")

# Setup logging
log_file = 'cbsl_rates.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(message)s'
)

def get_current_time():
    return datetime.now(sri_lanka_tz).strftime('%Y-%m-%d %H:%M:%S')

def log_usd_exchange_rate():
    iframe_url = 'https://www.cbsl.gov.lk/cbsl_custom/charts/usd/indexsmall.php'
    try:
        response = requests.get(iframe_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # The rate is somewhere in the iframe page, likely inside a div or text
        # Let's search for a pattern like "USD/LKR = 1 USD =  298.5000 LKR" or similar

        text = soup.get_text(separator=' ', strip=True)
        # A regex to find a number that looks like a rate (e.g. 298.5000)
        match = re.search(r'(\d{2,3}\.\d{1,4})', text)
        current_time = get_current_time()
        if match:
            rate = match.group(1)
            log_entry = f"{current_time} - USD/LKR Exchange Rate: {rate}"
            logging.info(log_entry)
            print(f"[LOGGED] {log_entry}")
        else:
            msg = f"{current_time} - USD rate not found in iframe content"
            logging.warning(msg)
            print(f"[WARNING] {msg}")
    except Exception as e:
        current_time = get_current_time()
        msg = f"{current_time} - Error fetching USD rate: {e}"
        logging.error(msg)
        print(f"[ERROR] {msg}")

def log_electricity_tariff():
    tariff_bands = [
        {"range": "0–30 kWh", "rate": 2.50, "fixed": 30},
        {"range": "31–60 kWh", "rate": 4.85, "fixed": 60},
        {"range": "61–90 kWh", "rate": 10.00, "fixed": 90},
        {"range": "91–120 kWh", "rate": 27.75, "fixed": 480},
        {"range": "121–180 kWh", "rate": 32.00, "fixed": 480},
    ]

    current_time = get_current_time()
    header = f"{current_time} - Electricity Tariff Bands:"
    logging.info(header)
    print(f"[LOGGED] {header}")

    for band in tariff_bands:
        line = f"{band['range']}: LKR {band['rate']} per kWh, Fixed: LKR {band['fixed']}"
        logging.info(f"{current_time} - {line}")
        print(f"[LOGGED] {line}")

if __name__ == '__main__':
    log_usd_exchange_rate()
    log_electricity_tariff()
