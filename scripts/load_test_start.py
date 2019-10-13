"Authon - Agam Jajoo"
"Version 0.1"


import pymqi, time,sys
from uuid import uuid4
import random
from pymqi import CMQC
from locust import HttpLocust, TaskSet, events
import datetime


from function1 import func1
from function2 import func2

# sys.path.append(r"D:\python27\Lib\site-packages\pymqi")

class UserBehavior(TaskSet):
	tasks = {func1: 30,
	func2 : 10,
	}

	# def on_start(self):
	# 	connection(self)
	#
	# def on_stop(self):
	# 	close_connection(self)

class WebsiteUser(HttpLocust):
	host = "http://abcd.com"
	task_set = UserBehavior
	min_wait = 1000
	max_wait = 1001
