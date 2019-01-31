# List Comprehensions

tasks = [
  {
    'name': 'Write for Envato Tuts+',
    'duration': 120
  },
  {
    'name': 'Work out',
    'duration': 60
  },
  {
    'name': 'Procrastinate on Duolingo',
    'duration': 240
  }
]

task_names = []
for task in tasks:
    task_names.append(task['name'])

task_names = [task['name'] for task in tasks]

difficult_tasks = []
for task in tasks:
    if task['duration'] >= 120:
        difficult_tasks.append(task['name'])

difficult_tasks = [task['name'] for task in tasks if task['duration'] >= 120]

result = [x ** y for x in [10, 20, 30] for y in [2, 3, 4]]
print(result)
