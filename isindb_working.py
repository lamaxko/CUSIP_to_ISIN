from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Folder paths
SourceFolder = "/Users/lasse/Desktop/CUSIP_to_ISIN/CUSIP_files"
DestinationFolder = "/Users/lasse/Desktop/CUSIP_to_ISIN/ISIN_files"

def main():
    # Instantiate a browser driver
    driver = webdriver.Chrome() # You may need to adjust this depending on your setup
    
    # Load data
    CUSIPs = load_data(SourceFolder)

    # Convert CUSIPs to ISINs
    ISINs = [cusip_to_isin(driver, cusip) for cusip in CUSIPs]
    
    # Save ISINs to csv
    save_data(DestinationFolder, ISINs)

    # Close the browser window
    driver.quit()

    print(ISINs)

def cusip_to_isin(driver, cusip):
    # Navigate to the ISIN database website
    driver.get("https://www.isindb.com/convert-cusip-to-isin/")

    # Find the input field and enter the CUSIP number
    input_field = driver.find_element(By.ID, "userinput")
    input_field.clear()
    input_field.send_keys(cusip)

    # Find the convert button and click it
    convert_button = driver.find_element(By.ID, "convert")
    convert_button.click()

    # Allow some time for the result to load
    time.sleep(1)  # This is a simple way to wait for the result. There are more robust methods available if needed.

    # Extract the ISIN number from the result
    result = driver.find_element(By.ID, "result")
    result_words = result.text.split()

    if len(result_words) < 5 or not result_words[4].startswith("US"):
        print(f"No valid ISIN found for CUSIP {cusip}")
        return None
    else:
        return result_words[4]

def load_data(SourceFolder):
    CUSIPs = []
    with open(SourceFolder + "/CUSIP_Numbers.csv") as f:
        for line in f:
            CUSIPs.append(line.strip())
    return CUSIPs

def save_data(DestinationFolder, ISINs):
    with open(DestinationFolder + "/ISIN_Numbers.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for isin in ISINs:
            writer.writerow([isin])

if __name__ == "__main__":
    main()
