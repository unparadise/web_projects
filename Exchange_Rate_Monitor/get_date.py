# Function returns the current date time
from datetime import datetime

def getDate():
    x = datetime.today()
    print(x)
    #x = datetime.now().strftime('%Y-%m-%d')
    #x = datetime.strptime(x, '%Y-%m-%d')

    return x