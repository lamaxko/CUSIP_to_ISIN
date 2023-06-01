# CUSIP to ISIN Converter

This Python script converts CUSIP numbers to ISINs using a web scraping method. 

## Prerequisites

Before running the script, you need to have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

You also need to install the required Python packages. Here's how to do it:

1. Open your terminal/command prompt.
2. Navigate to the directory where you've saved this script (use `cd` command).
3. Run `pip install -r requirements.txt`

Note: The Selenium package requires a driver to interface with the chosen browser. Chrome, for example, requires chromedriver, which needs to be installed and placed in the system's PATH. 

## How to use

1. Save your CUSIP numbers in a CSV file. You should place this file in a folder called 'CUSIP_files' located in the same directory as the script.
2. Run the script using Python in your terminal/command prompt like this: `python3 isindb_working.py`.
3. The script will create a new CSV file in the 'ISIN_files' folder (which it will create if doesn't exist) with your converted ISIN numbers.

## Troubleshooting

- If you're getting an error, make sure you've followed all the steps in the 'How to use' section correctly.
- Make sure you've installed all required packages with the `pip install -r requirements.txt` command.
- If you have any issues with the script, feel free to open an issue in this repository.

## Contributions

Contributions are always welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the [MIT License](LICENSE).
