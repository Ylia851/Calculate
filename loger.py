from datetime import datetime as dt
from time import time 
from algoritm import res

logfile = 'log.txt'
file = None

def Loger(data):
    data = dt.now().Strftime('%H:%M')
    with open ('log.txt', 'a') as file:
        file.write(f'res {res}')

            