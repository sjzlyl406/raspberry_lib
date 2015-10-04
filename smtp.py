#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
send txt email
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

sender = 'sjzlyl406@163.com'
#reveiver= 'sjzlyl406@163.com'
receiver= 'raspberry_leon@sina.com'

now = datetime.now()

subject='Ubuntu 14.04 ifconfig message'+now.strftime('%Y-%m-%d %H:%M:%S')
smtpserver='smtp.163.com'
username='sjzlyl406'
password='lyl316643'

import subprocess, re


def ifconf():
    cmd = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = cmd.communicate()
    memory = out.splitlines()
    ret = ""
    for line in memory:
        ret += line.decode('utf-8','ignore')
        ret += '\n'
    return ret

def re_ip():
    r_ip = re.compile('''((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))''')
    ipaddr = r_ip.findall(ifconf())
    if ipaddr:
        ret_str=""
        for ip_one in ipaddr:
            ret_str += "IP: " + str(ip_one) + "\n"
        return ret_str
    else:
        return "no ip"

msg = MIMEText(re_ip(),'plain')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

if __name__ == '__main__':
    smtp = smtplib.SMTP(smtpserver)
    ##smtp.set_debuglevel(1)
    smtp.docmd('ehlo', sender)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
