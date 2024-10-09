import csv
import os
import sys

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2"s urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def store_active_companies():
    url = (f"https://financialmodelingprep.com/api/v3/stock_market/actives?apikey={os.environ['FMP_API_KEY']}")
    data = get_jsonparsed_data(url)
    csv_file = "active_companies.csv"
    # Writing to the CSV file
    with open(csv_file, mode="w", newline="") as file:
        # Create a CSV DictWriter object, with fieldnames as the keys from the first dictionary
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write the header (column names)
        writer.writeheader()
        
        # Write each dictionary (row) to the CSV file
        writer.writerows(data)
    
    print(f"Data successfully written to {csv_file}")

if __name__ == "__main__":
    if "--run_job" in sys.argv:
        store_active_companies()