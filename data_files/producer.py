from celery import Celery
import consumer

app_name = 'consumer'  
app = Celery(app_name, broker=consumer.redis_url)


for i in range(100):
    a = 1
    b = 2
    consumer.consume.delay(a, b)
