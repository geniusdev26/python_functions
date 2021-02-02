import datetime
input("Enter number of seconds: ")
def convert(Sekunde):
    return str(datetime.timedelta(seconds = Sekunde))
print(convert(Sekunde))