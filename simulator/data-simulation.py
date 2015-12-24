'''
Created on Dec 23, 2015

@author: purushottamchaudhary
'''
import json
import time
import random
import requests



class humid_temp_loca_data(object):
    def __init__(self):
        self.h_data = None
        self.t_data = None
        self.l_data = None
        self.current_time = None


humidityData = {}
tempratureData = {}
locationData = {}
current_time = {}

#proxies = {
#  "http": "http://3.20.109.242:9400"
#}

flag = 1
while flag == 1:
    HTLT_DATA = humid_temp_loca_data()
    for sim in range(1, 11):
        # humidity object preparation
        humidityData['humidity'] = 25 + random.randint(0,9)
        humidityData['name'] = 'sim' + str(sim) + '_humidity'

        # temprature Data preparation
        tempratureData['temprature'] = 25 +  random.randint(0,9)
        tempratureData['name'] = 'sim' + str(sim) + '_temprature'

        # GPS data
        locationData['lang'] = '4121241.2412'
        locationData['latt'] = '3423423.123'
        locationData['name'] = 'sim' + str(sim) + '_location'

        # Current Time Stamp
        current_time = int(time.time() * 1000)

        HTLT_DATA.h_data = humidityData
        HTLT_DATA.t_data = tempratureData
        HTLT_DATA.l_data = locationData
        HTLT_DATA.current_time = current_time

        # meta-data for Request 
        #headers = {'content-type': 'application/json'}
        url = 'http://cargo-monitoring-dataingestion.run.aws-usw02-pr.ice.predix.io/SaveTimeSeriesData'
        #url = 'http://localhost:9191/SaveTimeSeriesData'
       # data = json.dumps(HTLT_DATA.__dict__)
        #print data
        params = {'clientId': 'admin', 'tenantId': '075841cb-d7fa-4890-84ea-fdd7d7c65b65', 'destinationId': 'TimeSeries','content-type': 'application/json','content':json.dumps(HTLT_DATA.__dict__)}
        # post data to server
        try:
            #response= requests.post(url, params=params, proxies=proxies)
            response= requests.post(url, params=params)

            print response 
        except Exception as x:
            print x    
    time.sleep(2)
