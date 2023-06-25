try:
    from re import T
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import csv
    import time
    import os
    import logging
except ImportError as e:
    print(f"ImportError: {e}")
    print("Please install the required packages and try again")
    raise SystemExit
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Folder paths
SOURCE_FOLDER = f"{str(os.getcwd())}/CUSIP_files"
DESTINATION_FOLDER = f"{str(os.getcwd())}/CUSIP_files_dest"

def main():
    logging.info("Program started (main)")
    logging.debug(f"SOURCE_FOLDER: {SOURCE_FOLDER}")
    logging.debug(f"DESTINATION_FOLDER: {DESTINATION_FOLDER}")
    logging.debug("Setting Selenium driver")

    # Instantiate a browser driver
    driver = webdriver.Chrome() # You may need to adjust this depending on your setup

    logging.debug("Loading data (Cusips)")
    # Load data
    CUSIPs = load_data(SOURCE_FOLDER)

    logging.debug("Converting CUSIPs to ISINs")
    # Convert CUSIPs to ISINs
    ISINs = [cusip_to_isin(driver, cusip) for cusip in CUSIPs]
    
    logging.debug("Saving ISINs to csv")
    # Save ISINs to csv
    save_data(DESTINATION_FOLDER, ISINs)

    logging.debug("Closing browser")
    # Close the browser window
    driver.quit()

    logging.info("Program finished (main)")
    print(ISINs)

def cusip_to_isin(driver, cusip):
    logging.info(f"Converting CUSIP {cusip} to ISIN")

    logging.debug("Navigating to ISIN database website")
    # Navigate to the ISIN database website
    driver.get("https://www.isindb.com/convert-cusip-to-isin/")

    logging.debug("Entering CUSIP number")
    # Find the input field and enter the CUSIP number
    input_field = driver.find_element(By.ID, "userinput")
    input_field.clear()
    input_field.send_keys(cusip)

    logging.debug("Clicking convert button")
    # Find the convert button and click it
    convert_button = driver.find_element(By.ID, "convert")
    convert_button.click()

    logging.debug("Waiting for result")
    # Allow some time for the result to load
    time.sleep(1)  # This is a simple way to wait for the result. There are more robust methods available if needed.

    logging.debug("Extracting ISIN number from result")
    # Extract the ISIN number from the result
    result = driver.find_element(By.ID, "result")
    result_words = result.text.split()

    logging.debug("Checking if ISIN number is valid")
    if len(result_words) < 5 or not result_words[4].startswith("US"):
        print(f"No valid ISIN found for CUSIP {cusip}")
        logging.warning(f"No valid ISIN found for CUSIP {cusip}")
        return None
    else:
        print(f"Found ISIN {result_words[4]} for CUSIP {cusip}")
        return result_words[4]

def load_data(SOURCE_FOLDER):
    logging.debug("Loading CUSIPs from csv")
    CUSIPs = []
    with open(SOURCE_FOLDER + "/CUSIP_Numbers.csv") as f:
        for line in f:
            CUSIPs.append(line.strip())
    return CUSIPs

def save_data(DESTINATION_FOLDER, ISINs):
    logging.debug("Saving ISINs to csv")
    with open(DESTINATION_FOLDER + "/ISIN_Numbers.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for isin in ISINs:
            writer.writerow([isin])

if __name__ == "__main__":
    logging.info("Program started (main)")
    st = time.time()
    main()
    en = time.time()
    logging.info(f"Program took {en-st} seconds to run")
    logging.info("Program finished (main)")
