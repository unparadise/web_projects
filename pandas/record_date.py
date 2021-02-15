from datetime import date

def recordDate(fileName):
    with open(fileName, 'w') as file:
        file.write(str(date.today()))
