import datetime
import csv
from forex_python.converter import CurrencyRates
import smtplib

exchangeRates = []
todaysRate = {'Date': None, 'Rate': 0, 'From': None, 'To': None}

def getDate():
    x = datetime.datetime.now()
    d = str(x.year) + '.' + str(x.month) + '.' + str(x.day)

    return d

def getRate(date, fromCurrency, toCurrency):
    """Retrieve the exchange rate from https://ratesapi.io.
    The function returns a dictionary object with date, rate,
    from, and to keys
    """

    c = CurrencyRates()
    rate = c.get_rate(fromCurrency, toCurrency)
    rate = format(rate, '.2f')

    return {'Date': date, 'Rate': rate, 'From': fromCurrency, 'To': toCurrency}



def sendemail(date, exRate, fmCurrency, toCurrency, receiverEmails): 
    """Send email to a specific address"""

    gmailSenderEmail = 'lianchen16@gmail.com'
    gmailPassword = 'iwayfbrismavabfy'
      
    emailSubject = 'Exchange rate alert!' 

    # creates SMTP session  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
      
    # start TLS for security  
    server.starttls()  
      
    # Authentication  
    server.starttls()  
      
    server.login(gmailSenderEmail, gmailPassword)  
      
    # message to be sent  
    headers = "\r\n".join(["from: " + gmailSenderEmail, 
                            "subject: " + emailSubject, 
                            "to: " + receiverEmails, 
                            "mime-version: 1.0", 
                            "content-type: text/html"]) 
      
    message = headers + 'The exchange rate from ' + fmCurrency + ' to ' + toCurrency + ' on ' + date + ' is ' + exRate
    
    try:
        server.sendmail(gmailSenderEmail, receiverEmails.split(','), message)
        print('Email sent')
    except SMTPException:
        print('Error: unable to send email')
    server.quit()


# This is the beginning of the main program

date = getDate()
#csvFile = './web_projects/Exchange_Rate_Monitor/exchange_rates.csv'
csvFile = './exchange_rates.csv'

try:
    with open(csvFile) as csvFileHandle:
        exchangeRates = csv.DictReader(csvFileHandle, delimiter=",")
        exchangeRates = list(exchangeRates)
except IOError:
    print('exchange_rates.csv file does not exist')
    
# If today is not in the exchangeRates list then add today's date,
# rate, from, and to data as a dictionary item to the list
if len(exchangeRates) == 0 or exchangeRates[len(exchangeRates)-1]['Date'] != date:
        todaysRate = getRate(date, 'USD', 'CNY')
        exchangeRates.append(todaysRate)
        if float(todaysRate['Rate']) < 7.0:
            sendemail(todaysRate['Date'], todaysRate['Rate'], todaysRate['From'], todaysRate['To'], 'lianchen16@gmail.com')

# Write the exchangeRates list to the exchange_rates.csv file
# TODO: Update the code to only write the new data
csvColumns = ['Date', 'Rate', 'From', 'To']
try:
    with open(csvFile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csvColumns)
        writer.writeheader()
        for data in exchangeRates:
            writer.writerow(data)
except IOError:
    print('Can\'t write to file. I/O error.')

print(exchangeRates)