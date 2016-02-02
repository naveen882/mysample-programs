from celery import Celery


app=Celery('tasks',backend='amqp',broker='amqp://')

@app.task(ignore_result=True)
def print_hello():
	print "hello there"

print_hello()


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results

#Refer https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
#usage: Run the following command on command line
#celery worker -A celery_ -n 1.%h &
#or
#celery worker -A celery_tasks -n 2.%h
#or
#celery worker -A celery_tasks &

#to kill the process
#ps aux|grep 'celery worker'|awk '{print $2}'|xargs kill #kill all completed tasks 
#OR
#ps aux|grep 'celery worker'|awk '{print $2}'|xargs kill -9   #force kill
