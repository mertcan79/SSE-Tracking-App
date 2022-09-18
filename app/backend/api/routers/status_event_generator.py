import asyncio
import uuid
import random

'''
Get status as an event generator
'''
status_stream_delay = 3  # second
status_stream_retry_timeout = 30000  # milisecond
topic_list = ['X','Y','Z']

async def status_event_generator(request, param1):
    previous_status = None
    while True:
        if await request.is_disconnected():
            break


        current_status = uuid.uuid1()
        #topic = random.choice(topic_list)
        topic = param1
        
        if previous_status != current_status:
            yield {
                "event": "update",
                "retry": status_stream_retry_timeout,
                "data": [topic,current_status]
            }
            previous_status = current_status
        else:
            pass
        await asyncio.sleep(status_stream_delay)