import csv
import requests
import threading
import json
from queue import Queue
import os
from dotenv import load_dotenv

load_dotenv()

# Function to call Pipfeed API and fetch article data
def fetch_article_data(url, api_key, queue):
    headers = {
        'accept': 'application/json',
        'x-magicapi-key': api_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"url": url})
    response = requests.post('https://api.magicapi.dev/api/v1/pipfeed/parse/extract', headers=headers, data=data)
    queue.put({'url': url, 'response': response.json()})

# Function to write data to CSV file
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'response']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

# Function to read URLs from CSV file
def read_urls_from_csv(input_file):
    urls = []
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            urls.append(row[0])
    return urls

# Main function to load URLs, fetch data, and write to CSV
def main(input_file, output_file, api_key):
    urls = read_urls_from_csv(input_file)
    data = []
    queue = Queue()
    threads = []

    # Create and start threads
    for url in urls:
        thread = threading.Thread(target=fetch_article_data, args=(url, api_key, queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Collect data from queue
    while not queue.empty():
        data.append(queue.get())

    # Write collected data to CSV
    write_to_csv(data, output_file)

# Run the script
if __name__ == "__main__":
    input_file = 'pipfeed-article-extract-demo/input.csv'
    output_file = 'pipfeed-article-extract-demo/output.csv'
    api_key = os.getenv('API_KEY')  # Get API key from environment variables
    main(input_file, output_file, api_key)
