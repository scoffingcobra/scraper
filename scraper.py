import requests
import pymongo
import logging
import json
from pymongo import MongoClient

# Setup logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["scraping_db"]
collection = db["scraped_data"]

def save_to_mongodb(page, data):
    try:
        collection.insert_one({"page": page, "data": data})
    except Exception as e:
        logging.error(f"Error saving to MongoDB: {e}")

def scrape_ajax_javascript():
    url = "https://www.scrapethissite.com/pages/ajax-javascript/#2015"
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Since it's AJAX, we need to simulate the dynamic content part
        # For simplicity, let's assume we can fetch data directly (adjust if needed)
        data = json.loads(response.text)
        save_to_mongodb("ajax_javascript", data)
    except Exception as e:
        logging.error(f"Error scraping AJAX JavaScript page: {e}")

def scrape_forms():
    url = "https://www.scrapethissite.com/pages/forms/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {"form_data": soup.prettify()}  # Replace with actual data extraction logic
        save_to_mongodb("forms", data)
    except Exception as e:
        logging.error(f"Error scraping Forms page: {e}")

def scrape_advanced():
    url = "https://www.scrapethissite.com/pages/advanced/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {"advanced_data": soup.prettify()}  # Replace with actual data extraction logic
        save_to_mongodb("advanced", data)
    except Exception as e:
        logging.error(f"Error scraping Advanced page: {e}")

def main():
    scrape_ajax_javascript()
    scrape_forms()
    scrape_advanced()

if __name__ == "__main__":
    main()
