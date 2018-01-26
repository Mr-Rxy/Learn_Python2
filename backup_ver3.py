#!/usr/bin/python
#coding=utf-8
# Filename: backup_ver2.py

import os
import time

source = ['/home/swaroop/byte', '/home/swaroop/bin']
target_dir = '/mnt/e/backup/'
if not  os.path.exists(target_dir):
	os.makedirs(target_dir)
	print 'Successfully created directory', target_dir
else:
	print '已存在', target_dir
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ','_' + '.zip')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
	print 'Backup FAILED'

