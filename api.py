from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from repos import Tasks, SubTasks


# use namedtuple to for records being read in from the database

# rename Tasks to TaskRepo - the objects constructed should represent the database connection not the task itself
# abstraction for the task is the namedtuple

class TextColors:
    RED = "\033[32m"
    GREEN = "\033[92m"
    END = "\033[0m"


class TaskCRUD:
    """Base class for CRUD operations"""

    def __init__(self, url='sqlite:///tasks'):
        engine = create_engine(url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

    def add_task(self, obj):
        """Persist task to database"""
        session.add(obj)
        session.commit()
        return True

    def edit_task(self, task_id, subtask=False, **kwargs):
        """Update task description, importance or date in database"""
        table = SubTasks if subtask else Tasks
        record = session.query(table).filter(id=task_id).update().values(**kwargs)
        return True

    def update_task(self, task_id, subtask=False, **kwargs):
        table = SubTasks if subtask else Tasks
        record = session.query(table).filter(id=task_id).update().values(**kwargs)
        session.commit()
        return True

    def list_task(cls, completed=False, subtask=False):
        """function to list all tasks"""
        columns = ["ID", "Description", "Deadline"]
        if completed is True:
            tasks = session.query(Tasks).filter(Tasks.subtasks.any(SubTasks.completed == False)). \
                order_by(Tasks.due_date).all()
        else:
            tasks = session.query(Tasks).filter_by(Tasks.completed != True). \
                filter(Tasks.subtasks.any(SubTasks.completed == False)).all()

        if not subtask:
            print(f"\u2554{'':\u2550<5}\u2566{'':\u2550<120}\u2566{'':\u2550<15}\u2566{'':\u2550<15}\u2557")
            print(f"\u2551{columns[0]:^5}\u2551{columns[1]:^120}\u2551{columns[2]:^15}\u2551{columns[3]:^15}\u2551")
            print(f"\u2560{'':\u2550<5}\u256C{'':\u2550<120}\u256C{'':\u2550<15}\u256C{'':\u2550<15}\u2563")
            for task in tasks:
                if tasks.high_priority:
                    print(f'\u2551{TextColors.RED}{task.id:<5}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.description:<120}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.due_date:<15}{TextColors.END}'
                          f'\u2551{TextColors.RED}{len(task.subtasks):<15}{TextColors.END}\u2551')
                if task.completed:
                    print(f'\u2551{TextColors.RED}{task.id:<5}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.description:<120}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.due_date:<15}{TextColors.END}'
                          f'\u2551{TextColors.RED}{len(task.subtasks):<15}{TextColors.END}\u2551')
                else:
                    print(f'\u2551{task.id:<5}'
                          f'\u2551{task.description:<120}'
                          f'\u2551{task.due_date:<15}'
                          f'\u2551{len(task.subtasks):<15}\u2551')
            print(f"\u255A{'':\u2550<5}\u2569{'':\u2550<120}\u2569{'':\u2550<15}\u2569{'':\u2550<15}\u255d")
        else:
            print(f"\u2554{'':\u2550<5}\u2566{'':\u2550<120}\u2566{'':\u2550<15}\u2566{'':\u2550<15}\u2557")
            print(f"\u2551{columns[0]:^5}\u2551{columns[1]:^120}\u2551{columns[2]:^15}\u2551{columns[3]:^15}\u2551")
            print(f"\u2560{'':\u2550<5}\u256C{'':\u2550<120}\u256C{'':\u2550<15}\u256C{'':\u2550<15}\u2563")
            for task in tasks:
                if tasks.high_priority:
                    print(f'\u2551{TextColors.RED}{task.id:<5}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.description:<120}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.due_date:<15}{TextColors.END}'
                          f'\u2551{TextColors.RED}{len(task.subtasks):<15}{TextColors.END}\u2551')
                if task.completed:
                    print(f'\u2551{TextColors.RED}{task.id:<5}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.description:<120}{TextColors.END}'
                          f'\u2551{TextColors.RED}{task.due_date:<15}{TextColors.END}'
                          f'\u2551{TextColors.RED}{len(task.subtasks):<15}{TextColors.END}\u2551')
                else:
                    print(f'\u2551{task.id:<5}'
                          f'\u2551{task.description:<120}'
                          f'\u2551{task.due_date:<15}'
                          f'\u2551{len(task.subtasks):<15}\u2551')
                for subtask in task.subtasks:
                    if subtask.high_priority:
                        print(f"\u2551{'':<5}\u2551{'':<5}"
                              f"{TextColors.RED}{subtask.description:<115}{TextColors.END}\u2551"
                              f"{TextColors.RED}{subtask.due_date:<15}{TextColors.END}\u2551"
                              f"{'':<15}\u2551")
                    else:
                        print(f"\u2551{'':<5}\u2551{'':<5}"
                              f"{subtask.description:<115}\u2551"
                              f"{subtask.due_date:<15}\u2551"
                              f"{'':<15}\u2551")
            print(f"\u255A{'':\u2550<5}\u2569{'':\u2550<120}\u2569{'':\u2550<15}\u2569{'':\u2550<15}\u255d")
        return True

# class SuperTask(Task):
#     def __init__(self, conn, obj):
#         super(SuperTask, self).__init__(conn, obj)
#
#     def add_task(self, conn, obj):
#         """Persist task to database - use conn to open a cursor then insert into table
#         Replace with an ORM implementation to decouple database schema and object model"""
#         conn.execute('''INSERT INTO tasks
#                           (description,
#                           due_date,
#                           high_priority,
#                           completed)
#                           VALUES
#                           (?, ?, ?, ?)''', (obj.description, obj.due_date, obj.high_priority, obj.completed))
#         conn.commit()
#         conn.close()
#         return True
#
#     def edit_task(self, conn, obj):
#         if obj.description is None:
#             if obj.high_priority is None:
#                 conn.execute('''UPDATE tasks
#                 SET due_date = ?
#                 WHERE id = ?
#                 ''', (obj.due_date, obj.id))
#             else:
#                 conn.execute('''UPDATE tasks
#                                 SET due_date = ?,
#                                 high_priority = ?
#                                 WHERE id = ?
#                                 ''', (obj.due_date, obj.high_priority, obj.id))
#         else:
#             if obj.high_priority is None:
#                 conn.execute('''UPDATE tasks
#                 SET
#                 description = ?,
#                 due_date = ?
#                 WHERE id = ?
#                 ''', (obj.description, obj.due_date, obj.id))
#             else:
#                 conn.execute('''UPDATE tasks
#                                 SET
#                                 description = ?,
#                                 due_date = ?,
#                                 high_priority = ?
#                                 WHERE id = ?
#                                 ''', (obj.description, obj.due_date, obj.high_priority, obj.id))
#         return True
#
#     def update_task(self, conn, obj):
#         """Mark task as complete or remove"""
#         if obj.completed is not None:
#             conn.execute('''UPDATE tasks
#             SET completed = ?
#             WHERE id = ?
#             ''', (obj.completed, obj.id))
#         if obj.remove is not None:
#             conn.execute('''DELETE FROM tasks
#             WHERE id = ?
#             ''', obj.id)
#         return True
#
#     def list_task(self, conn, *, task_id=None, list_all=False, completed=False, subtasks=False):
#         if task_id is True and list_all is True:
#             return f"Can't list all tasks and {task_id} at the same time."
#         if task_id is True:
#             tasks = conn.execute('''SELECT * FROM tasks WHERE id = ?''', task_id)
#             print(task for task in tasks)
#             if subtasks is True:
#                 SubTask.list(task_id, completed)
#         elif list_all is True:
#             super.list(completed, subtasks)
#
#
# class SubTask(Task):
#
#     @classmethod
#     def list(cls, super_id, completed):
#         return None
