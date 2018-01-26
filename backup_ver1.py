#!/usr/bin/python
#coding=utf-8
# Filename: backup_ver1.py
import os
import time
# 哈哈
source = ['/home/swaroop/byte', '/home/swaroop/bin']

target_dir = '/mnt/e/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
