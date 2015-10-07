#!/usr/bin/env python
# -_-!! coding: utf-8 -_-!!

import linecache
import time

start_time = time.time()    #coding start

# 前期准备， 整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')
keys = {data_keys[k]:k for k in range(0, len(data_keys))}
f = linecache.getlines('twitter数据挖掘片段.txt')
lines = [x[1:-1].split('","') for x in f]


#1 输出用户数
users = set(line[keys['username']] for line in lines)
user_total = len(set(users))
print "用户数：%d" % int(user_total)


#2 每一个用户的名字 list
name_list = list(users)
print name_list[0].decode('utf-8')


#3 有多少个2012年11月发布的twitters
twitter_total = len([line for line in lines if line[keys['created_at']].startswith('2012-11')])
lines_from_2012_11 = len(filter(lambda line:line[keys['created_at']].startswith('2012-11'),lines))
print lines_from_2012_11
print twitter_total


#4 该文本里， 有那几天的数据
uniq_date = list(set([line[keys['created_at']].split(' ')[0] for line in lines]))
uniq_date.sort()
print uniq_date[0]


#5 该文本里，在那个小时发布的数据最多？
hours = [int(hour[keys['created_at']][11:13]) for hour in lines]
hours_total = [(h, hours.count(h)) for h in xrange(0, 24)]
hours_total.sort(key=lambda x: x[1], reverse = True)
print '发布数据最多的小时是:%s ' % hours_total[0][0]


#6 该文本中， 输出在每一天发表twitter最多的用户
'''
date_list = [line[keys['created_at']][0:10] for line in lines]
ret = []
for date in list(set(date_list)):
    name_list = [line[keys['username']] for line in lines if line[keys['created_at']].startswith(date)]
    name_puple = [(name, name_list.count(name)) for name in list(set(name_list))]
    name_puple.sort(key=lambda x: x[1], reverse=True)
    ret.append((date, name_puple[0][0]))
print '在%s发表最多的用户是:%s' % (ret[0][0], ret[0][1])
'''

dateline_by_user = {k:dict() for k in uniq_date}
for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].has_key(username):
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1
for k,v in dateline_by_user.items():
    us = v.items()
    us.sort(key=lambda k:k[1],reverse=True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}
print '在%s发表最多的用户是:%s' % ('2011-08-22',dateline_by_user['2011-08-22'].keys()[0])


#7 请按照时间顺序输出2012-11-03每个小时发布twitter的频率
hour_per = [int(line[keys['created_at']][11:13]) for line in lines if line[keys['created_at']].startswith('2012-11-03')]
freq_post_2012_11_03 = [(hour, hour_per.count(hour)) for hour in xrange(0, 24)]
print freq_post_2012_11_03

lines_from_2012_11_03 = filter(lambda line:line[keys['created_at']].startswith('2012-11-03'),lines)
hourlines_from_2012_11_03 = {str(i):0 for i in xrange(0,24)}
for line in lines_from_2012_11_03:
    hour = line[keys['created_at']][11:13]
    hourlines_from_2012_11_03[str(int(hour))] += 1 
hour_timeline_from_2012_11_03 = [(k,v) for k,v in hourlines_from_2012_11_03.items()]
hour_timeline_from_2012_11_03.sort(key=lambda k:int(k[0]))
print hour_timeline_from_2012_11_03


#8 统计该文本里， 来源的相关信息与次数
source_list = [line[keys['source']] for line in lines]
source_ret = [(x, source_list.count(x)) for x in list(set(source_list))]
print source_ret[0]


#9 计算转发的url中：以：“http://twitter.com/umiushi_no_uta”开头的由几个
num = len([line for line in lines if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta')])
print num

#10 UID为573638104的用户发了多少个微博
num = len([line for line in lines if line[keys['uid']] == '573638104'])
print num
