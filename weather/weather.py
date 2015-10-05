#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    在terminal窗口输出获得的天气信息
    api接口:http://apistore.baidu.com/apiworks/servicedetail/478.html
    通过city变量修改城市
'''

import urllib2, json, sys

def getmsg(city):
    apikey = "cac4d58cc23bd8e8c6a829bd2d93778a"
    url = 'http://apis.baidu.com/heweather/weather/free?city=%s' % city

    req = urllib2.Request(url)
    req.add_header("apikey", apikey)

    resp = urllib2.urlopen(req)
    content = json.load(resp)
    return content

def basicinfo(content):
    print '---------basic------------'
    print 'city: %s' % content['HeWeather data service 3.0'][0]['basic']['city']
    print 'lat: %s ' % content['HeWeather data service 3.0'][0]['basic']['lat']
    print 'lon: %s ' % content['HeWeather data service 3.0'][0]['basic']['lon']
    print 'update time: %s ' % content['HeWeather data service 3.0'][0]['basic']['update']['loc']

def weatherinfo(content):
    print '----------weather-----------'
    print 'weather now: %s' % content['HeWeather data service 3.0'][0]['now']['cond']['txt']
    print u'体感温度 now: %s' % content['HeWeather data service 3.0'][0]['now']['fl']
    print u'温度 now: %s' % content['HeWeather data service 3.0'][0]['now']['tmp']
    print u'相对湿度 now: %s %%' % content['HeWeather data service 3.0'][0]['now']['hum']
    print u'能见度 now: %s km' % content['HeWeather data service 3.0'][0]['now']['vis']
    print 'wind now: %s' % content['HeWeather data service 3.0'][0]['now']['wind']['dir']

if __name__ == '__main__':
    city = "changan"
    if len(sys.argv) > 1:
        city = sys.argv[1]

    content = getmsg(city)
    if content['HeWeather data service 3.0'][0]['status'] == 'ok':
        basicinfo(content)
        weatherinfo(content)
    else:
        print content['HeWeather data service 3.0'][0]['status']
