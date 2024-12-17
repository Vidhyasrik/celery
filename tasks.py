from celery import Celery
import time
print("file Name:=>", __file__)
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0' )

@app.task
def my_task(arg1, arg2):
    # Task logic here
    return arg1 + arg2

@app.task
def long_running_task(arg):
    time.sleep(10)  # Simulate a long-running task
    return arg * 2

@app.task
def process_results(results):
    # Process the results from multiple tasks
    total = sum(results)
    return total