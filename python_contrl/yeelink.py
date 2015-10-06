#!/usr/bin/python
# -*- coding: utf-8 -*-

"send cpu temperature to yeelink every 60 sec"

import time, json, requests

api_url = 'http://api.yeelink.net/v1.0'
api_key = '*****************************'
api_headers = {'U-ApiKey':api_key,'content-type':'application/json'}
raspi_device_id = 340880
cpu_sensor_id = 377798


def get_cpu_temp():
    cpu_temp_file = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp = cpu_temp_file.read()
    cpu_temp_file.close()
    return float(cpu_temp)/1000

def upload_cpu_temp_to_yeelink():
    url = r'%s/device/%s/sensor/%s/datapoints' % (api_url, raspi_device_id, cpu_sensor_id)
    strftime = time.strftime("%Y-%m-%d %H:%M:%S")
    print "time:", strftime
    cpu_temp = get_cpu_temp()
    print "cpu_temp:", cpu_temp
    data = {'timestamp':strftime, 'value':cpu_temp}
    res = requests.post(url, headers=api_headers, data=json.dumps(data))
    print "status_code:", res.status_code

def main():
    while True:
        upload_cpu_temp_to_yeelink()
        time.sleep(60)

if __name__ == '__main__':
    main()
