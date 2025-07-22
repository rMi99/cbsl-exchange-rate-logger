# CBSL Exchange Rate Logger

A simple Python script to fetch and log the current USD to LKR exchange rate from the Central Bank of Sri Lanka (CBSL) website, along with logging the current electricity tariff bands.

## Features

- Scrapes the USD/LKR exchange rate from CBSL's official iframe page.
- Logs the exchange rate with timestamps in Sri Lanka timezone.
- Logs predefined electricity tariff bands.
- Logs are saved to `cbsl_rates.log` file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pytz` library

## Installation

Install required Python packages using pip:

```bash
pip install requests beautifulsoup4 pytz
