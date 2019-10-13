"Authon - Agam Jajoo"
"Version 0.1"



import pymqi, time
from uuid import uuid4
import random
import cx_Oracle
import datetime
from datetime import datetime , date
from locust import events
import logging
# import newrelic.agent

# logging.info (time.time())


# @newrelic.agent.background_task()
def func2(num):
    now_time = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
	# print (time.asctime())
    start_time = time.time()
    line = """any text
	"""

    req_id = uuid4().hex



    " ***************** QA1 Env *****************"
    host = "your host name for queue manager"
    port = "port name for queue manager"
    channel = "channel name foe queue manager 01N"
    queue_manager = "queue manager name.MQ"
    queue_name = "request queue where you want to send a message"
    " *******************************************"


    conn_info = "%s(%s)" % (host, port)
    qmgr = pymqi.connect(queue_manager, channel, conn_info)
    queue = pymqi.Queue(qmgr, queue_name)
    queue.put(formated_line)

    queue.close()
    qmgr.disconnect()
    total_time = int ((time.time() - start_time) * 1000)
    events.request_success.fire (request_type = 'transaction name' , name = 'request' , response_time = total_time , response_length = 0)


