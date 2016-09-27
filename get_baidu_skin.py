#! /usr/env/bin python
#! _*_ coding:utf-8 _*_

import os
import string, urllib2
import datetime
import threading

image_path = os.getcwd() + "/baidu_skin_image/"

thread_count = 20

total = 520

def SavePic(picUrl, picName):
	picFile = image_path + picName + '.jpg'

	global html
	
	try:
		html = urllib2.urlopen(picUrl).read()

		if html.find("您要访问的页面不存在") == -1:
			print 'begin download:' + picName + '.jpg'

			f = open(picFile, 'w+')
			f.write(html)
			f.close()
	except:
		print 'Get picture faild:' + picUrl

def LoopDownPic(start, max):
	for i in range(max):
		if i > start:
			SavePic("https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG/skin/%d.jpg" % i, str(i))

def getPageNumber():
	if total <= thread_count:
		return 1
	t = total / thread_count
	if total % thread_count > 0:
		t += 1
	return t

def main():
	print '=================Start download================='

	if not os.path.exists(image_path):
		os.makedirs(image_path)

	startTime = datetime.datetime.now()

	totalPageNumber = int(getPageNumber())

	i = 0

	while i < thread_count:
		t = threading.Thread(target = LoopDownPic, args = (i * totalPageNumber, totalPageNumber * (i + 1) + 1))
		t.start()
		i += 1

	t.join()

	#loopPic()

	endTime = datetime.datetime.now()

	print '=================Over, Cost time:' + str((endTime - startTime).seconds) + 's ================='

if __name__ == "__main__":
	main()