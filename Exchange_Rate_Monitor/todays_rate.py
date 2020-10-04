import datetime
import csv
from get_date import getDate
from save_rates import saveRates
from get_rate import getRate
from send_email import sendEmail
import tkinter as tk

window = tk.Tk()
window.geometry("260x160")
window.title("Today's Exchange Rate")

frameTitle = tk.Frame(master=window)
frameResult = tk.Frame(master=window)

labelTitle = tk.Label(master=frameTitle, text="USD/RMB Exchange Rate")
labelExchangeRate = tk.Label(master=frameResult)

def todayRate():
    exchangeRates = []
    todaysRate = {'Date': None, 'Rate': 0, 'From': None, 'To': None}
    alertRate = 7.0

    date = getDate()
    #csvFile = './web_projects/Exchange_Rate_Monitor/exchange_rates.csv'
    csvFile = './exchange_rates.csv'
    csvColumns = ['Date', 'Rate', 'From', 'To']

    try:
        with open(csvFile) as csvFileHandle:
            exchangeRates = csv.DictReader(csvFileHandle, delimiter=",")
            exchangeRates = list(exchangeRates)
    except IOError:
        print('exchange_rates.csv file does not exist')
    
    # If today is not in the exchangeRates list then add today's date,
    # rate, from, and to data as a dictionary item to the list
    ## TODO: move the code that decides whether there is new data to the save_rates.py file
    if len(exchangeRates) == 0 or exchangeRates[len(exchangeRates)-1]['Date'] != str(date):
        todaysRate = getRate(date, 'USD', 'CNY')
        exchangeRates.append(todaysRate)
        #if float(todaysRate['Rate']) < alertRate:
        #    sendEmail(todaysRate['Date'], todaysRate['Rate'], todaysRate['From'], todaysRate['To'], 'lianchen16@gmail.com')

        # Write the exchangeRates list to the exchange_rates.csv file
        saveRates(exchangeRates, csvFile, csvColumns)
        labelExchangeRate.config(text=str(date) + ': ' + todaysRate['Rate'])
        return True

    else:
        print('Today\'s rate is already retrieved.')
        #print(str(date) + ': ' + exchangeRates[len(exchangeRates)-1]['Rate'])
        labelExchangeRate.config(text=str(date) + ': ' + exchangeRates[len(exchangeRates)-1]['Rate'])
        return True


labelTitle.pack(padx=10, pady = 10)
btnTodayRate = tk.Button(master=frameTitle, text="Display rate", command=todayRate)
btnTodayRate.pack(padx= 10)

labelExchangeRate.pack(padx=10)
frameTitle.pack(fill=tk.BOTH, expand=True)
frameResult.pack(fill=tk.BOTH, expand=True)

window.mainloop()