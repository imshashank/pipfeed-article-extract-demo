# Pipfeed Article Extractor

This script uses the Pipfeed API to extract and summarize articles from URLs provided in a CSV file. The results are saved to another CSV file. Follow the instructions below to set up and run the script.

###  Documentation 
You can find the documentation for this API at [Pipfeed](https://docs.api.market/api-product-docs/magicapi/pipfeeds-extract-api-developer-documentation)

### Run through Replit
You can run this whole script through [replit](https://replit.com/@hello737/Pipfeed-article-extract#pipfeed-article-extract-demo/main.py)

## What This Script Does

- Reads a list of URLs from an `input.csv` file.
- Uses the Pipfeed API to extract article summaries.
- Writes the extracted data to an `output.csv` file.

## Requirements

- Python 3.x
- install with `pip install requirements.txt`

## How to Use

### Option 1: Clone the GitHub Repository

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/imshashank/pipfeed-article-extract-demo.git
   ```

2. **Prepare Your Input File:**
   Ensure your `input.csv` file is in the same directory as the script. This file should contain the URLs of the articles you want to process, one URL per line:
   ```csv
   https://www.example.com/article1
   https://www.example.com/article2
   ...
   ```
   We already have an input file in this github repo which you can just clone. 


3. **Get Your API Key:**
   Sign up for an account at [Api.market](https://api.market/) to obtain your API key.
   Just go to the left hand section called `🔑 API Keys` and copy your API KEY.



4. **Subscribe to Pipfeed API**
   Subscribe to pipfeed api to use it through this script at [Pipfeed](https://api.market/store/pipfeed/parse).



5. **Update the Script:**
   Replace the placeholder `YOUR_API_KEY_HERE` in the `.env` file with your actual API key.


6. **Install Dependencies:**
   ```bash
   pip3 install requirements.txt
   ```

7. **Run the Script:**
   ```bash
   python3 main.py
   ```

### Option 2: Use Replit

1. **Fork the Replit Project:**
   Go to [Replit](https://replit.com/@hello737/Pipfeed-article-extract#pipfeed-article-extract-demo/main.py) and fork the project.

2. **Prepare Your Input File:**
   Add your `input.csv` file to the Replit workspace. This file should contain the URLs of the articles you want to process, one URL per line. We already have an `input.csv` file in the replit workspace.
   ```csv
   https://www.example.com/article1
   https://www.example.com/article2
   ...
   ```

3. **Get Your API Key:**
   Sign up for an account at [Api.market](https://api.market/) to obtain your API key.
   Just go to the left hand section called `🔑 API Keys` and copy your API KEY.


4. **Subscribe to Pipfeed API**
   Subscribe to pipfeed api to use it through this script at [Pipfeed](https://api.market/store/pipfeed/parse).


4. **Update the Script:**
   Replace the placeholder `YOUR_API_KEY_HERE` in the `.env` file with your actual API key.
   `.env` is usually hidden by replit so make sure to unhide the file and then replacing your API Key in there. 


5. **Run the Script:**
   Click the "Run" button in Replit.



### Notes

- Ensure your input file is named input.csv.
- The script can process up to 100 URLs.
- Modify the script if you need to handle more URLs or customize the API request/response handling.

### About Pipfeed API

The Pipfeed API extracts main article content and metadata from news and blogs. It handles geo-restrictions and client-side rendering, providing clean JSON data with titles, summaries, text, and other properties. This allows you to avoid the hassle of web scraping and focus on building your applications.

For more details, visit the Pipfeed API [documentation](https://docs.api.market/api-product-docs/magicapi/pipfeeds-extract-api-developer-documentation).



That's it! The script will read URLs from `input.csv`, process them using the Pipfeed API, and write the results to `output.csv`.
