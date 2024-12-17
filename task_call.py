# from .tasks import my_task
from tasks  import long_running_task, process_results, my_task


res = my_task.delay(20,30)

print("Celery Results are:", res.get())

result1 = long_running_task.delay(10)
result2 = long_running_task.delay(20)

# Wait for both tasks to finish and collect their results
results = [result1.get(), result2.get()]

# Send the results to the `process_results` task
final_result = process_results.delay(results)
print(final_result.get())  # Will print 60

