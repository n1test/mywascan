#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

from os import path
from re import search
from lib.utils.check import *
from lib.utils.printer import *
from lib.utils.readfile import *
from lib.request.request import *
import httplib
import sys

class webports(Request):
	""" webports  """
	get = "GET"
	def __init__(self,kwargs,url,data):
		Request.__init__(self,kwargs)
		self.url = url 
		self.data = data

	def search(self):
		""" Search Path """
		_ = None
		realpath = path.join(path.realpath(__file__).split('plugins')[0],'lib/db/')
		return (realpath+"phpinfo.wascan")

	def run(self):
		""" Run """
		info('Checking Ports Open...')
		output = sys.stdout
		for i in range(1,65535):
 			#rate=i/65535
 			output.write('\rcheck Port:%.0f' % i)
 			output.flush()

			try:			
				url = '%s:%s'%(self.url[7:-1],str(i))
				#plus('Checking Port Open at: %s'%(url))
				#req = self.Send(url=url,method=self.get,)
				c = httplib.HTTPConnection(url)
				c.request("HEAD", '')
#			if req.code == 200:
				if c.getresponse().status == 200:
						plus('Found Port Open at: %s'%(url))
						c.close()
						#continue
			except (httplib.HTTPException, socket.error) as ex:
				#print "Error: %s" % ex
				continue

"""
		for path in readfile(self.search()):
			# check url path
			url = CPath(self.url,path)
			# send request 
			req = self.Send(url=url,method=self.get,)
			# if status code == 200
			if req.code == 200:
				# and search in req.content
				if search(r'\<title\>phpinfo()\<\/title\>|\<h1 class\=\"p\"\>PHP Version',req.content):
					plus('Found phpinfo page at: %s'%(req.url))
					break
"""