# This function save the dictionary data passed to it
import csv

## TODO: Update the code to only write the new data

def saveRates(rates, file, csvColumns):
    try:
        with open(file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=csvColumns)
            writer.writeheader()
            for data in rates:
                writer.writerow(data)
    except IOError:
        print('Can\'t write to file. I/O error.')