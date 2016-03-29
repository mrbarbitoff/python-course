#!/usr/bin/env python3

import pyowm
import re
from time import ctime
import argparse

parser = argparse.ArgumentParser(description='Show weather and forecast in specified city')
parser.add_argument("city",  
                    type=str, 
                    default='Saint-Louis', 
                    nargs='?', 
                    help='specify the city to look for weather in')
parser.add_argument("--day", 
                    type=int, 
                    default=0, 
                    choices=[0, 1, 2, 3, 4], 
                    help='show weather for 0 - today, 1 - tomorrow, 2-4 - X days afterwards')

args=parser.parse_args()
city = args.city
day = args.day

def fancy_time(obj):
    thistime = ctime(obj.get_reference_time())
    this_temp = obj.get_temperature(unit='celsius')['temp']
    this_status = obj._detailed_status
    return '%s, %s градусов Цельсия и %s' % (thistime, this_temp, this_status)
   
owm = pyowm.OWM('c5483c8fbde0cc8775399183e2e7c7e3')
forecasts = []
fc = owm.three_hours_forecast(city)
f = fc.get_forecast()
for weather in f:
    forecasts.append(fancy_time(weather))

# fucking OK
date_start = forecasts[0][4:10]
for i, fc in enumerate(forecasts):
    if date_start not in fc:
        break
if day == 0:
    for time_point in forecasts[0:i]:
        print(time_point)
else:
    print('\n'.join(forecasts[(i + (day - 1) * 8):(i + day * 8)]))
