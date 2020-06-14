# Function sends an email to alert the person that the exchange rate
# has passed the defined threshold


import smtplib

def sendEmail(date, exRate, fmCurrency, toCurrency, receiverEmails): 
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