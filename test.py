import pytest
import csv
import os
from main import main

@pytest.fixture
def setup_test_files():
    input_file = 'test_input.csv'
    output_file = 'test_output.csv'

    # Create a sample input CSV file
    with open(input_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['https://techcrunch.com/2022/04/18/web-scraping-legal-court/'])
        writer.writerow(['https://www.cnn.com/2022/03/10/health/covid-community-levels-cdc/index.html'])

    yield input_file, output_file

    # Clean up test files
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)

def test_pipfeed_api(setup_test_files):
    input_file, output_file = setup_test_files
    api_key = 'clusi6tp60003lb0c12wnt8ss'  # Replace with your actual Pipfeed API key

    # Run the main function to process the input CSV and create the output CSV
    main(input_file, output_file, api_key)

    # Check if output CSV file is created
    assert os.path.exists(output_file)

    # Load the output CSV file and check the content
    with open(output_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 2  # Check if there are 2 rows
        for row in rows:
            assert 'url' in row
            assert 'response' in row
