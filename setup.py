import sqlite3

conn_tasks = sqlite3.connect('tasks.db')
conn_subtasks = sqlite3.connect('subtasks.db')

c1 = conn_tasks.cursor()
c2 = conn_subtasks.cursor()

c1.execute('''CREATE TABLE tasks 
    (id integer primary key, 
    description text, 
    due_date text, 
    high_priority text, 
    completed text)''')

c2.execute('''CREATE TABLE subtasks
    (id integer primary key, 
    foreign key(task_id) references tasks(id),
    description text, 
    due_date text, 
    high_priority text, 
    completed text)''')

conn_tasks.close()
conn_subtasks.close()

# sqlite3.register_converter() and sqlite3.register_adapter() to convert timestrings
# row_factory = sqlite3.Row


