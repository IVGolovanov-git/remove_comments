







import re


from glob import glob


file_list = glob('task_*.md')
file_list.sort()


task_reg = re.compile('Задача(.*)Решение', re.MULTILINE | re.DOTALL)

decision_reg = re.compile('Решение(.*)Подсказки', re.MULTILINE | re.DOTALL)

for file_name in file_list:
task_id = int(file_name.split('_')[1][:-3])

with open(file_name, 'r', encoding='utf-8') as f:
file_text = f.read()


task = re.findall(task_reg, file_text)[0].strip()

decision = re.findall(decision_reg, file_text)[0].strip()


with open('all_tasks.md', 'a') as f:
f.write(f'Задача №{task_id}\n\
Задание {task_id}:\n{task}\n\
Решение {task_id}:\n{decision}\n')


with open('tasks.log', 'a') as f:
f.write(f'Задание из файла: {file_name} успешно загружено \n')
