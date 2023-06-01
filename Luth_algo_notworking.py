import csv

# Path to the directory containing the input CUSIP data.
SourceFolder = "/Users/lasse/Desktop/CUSIP_to_ISIN/CUSIP_files"

# Path to the directory where the output ISIN data will be saved.
DestinationFolder = "/Users/lasse/Desktop/CUSIP_to_ISIN/ISIN_files"

def main():
    """Main function of the script.
    Loads CUSIP data, converts each CUSIP to an ISIN, then saves the ISINs.
    """
    # Load CUSIP data from CSV file.
    CUSIPs = load_data(SourceFolder)

    # Convert each CUSIP to an ISIN.
    ISINs = [cusip_to_isin(cusip) for cusip in CUSIPs]

    # Save the converted ISINs to a new CSV file.
    save_data(DestinationFolder, ISINs)

    # Print the converted ISINs to the console.
    print(ISINs)

def cusip_to_isin(cusip):
    base = 'US' + cusip
    total = 0
    for i, c in enumerate(base[::-1]):
        if c.isdigit():
            n = int(c)
        else:
            n = ord(c) - 55
        if i % 2 == 0:
            n *= 2
        total += n // 10 + n % 10
    check_digit = (10 - (total % 10)) % 10
    return base + str(check_digit)







def load_data(SourceFolder):
    """Loads CUSIP data from a CSV file."""
    CUSIPs = []
    with open(SourceFolder + "/CUSIP_Numbers.csv") as f:
        for line in f:
            CUSIPs.append(line.strip())
    return CUSIPs

def save_data(DestinationFolder, ISINs):
    """Saves ISIN data to a CSV file."""
    with open(DestinationFolder + "/ISIN_Numbers.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for isin in ISINs:
            writer.writerow([isin])

# If this script is run directly (as opposed to being imported), then the main function is called.
if __name__ == "__main__":
    main()

"""234567879
234567869
234557819
233567819
445678901
345678901
845678901
845678911
345688901
456784012
466789012
556789012
456789112
356789012
456459012"""