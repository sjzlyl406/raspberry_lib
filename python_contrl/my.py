#!/usr/bin/python
# -*- coding: utf-8 -*-

"如果联网，执行smtp模块中的smtpfuc()函数"

import os
from smtp import smtpfuc

if __name__ == '__main__':
	ret = os.system('ping -c3 www.baidu.com')
	count = 3
	while ret != 0 and count != 0:
		ret = os.system('ping -c3 www.baidu.com')
		count -= 1
	if count == 0:
		print 'fail'
	else:
		smtpfuc()
