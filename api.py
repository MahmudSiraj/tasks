from datetime import datetime
from typing import NamedTuple

# use namedtuple to for records being read in from the database


class TaskRecord(NamedTuple):
    id: int
    description: str
    due_date: datetime
    high_priority: bool
    completed: bool


class SubtaskRecord(NamedTuple):
    id: int
    task_id: int
    description: str
    due_date: datetime
    high_priority: bool
    completed: bool


class Task:
    """Super class for both tasks and subtasks. Constructs a task and provides skeleton CRUD operations."""

    def __init__(self, conn, obj):
        self.conn = conn
        TaskRecord.description = obj.description
        TaskRecord.due_date = datetime(obj.due_date)
        TaskRecord.high_priority = obj.high_priority
        TaskRecord.completed = obj.completed

    def add_task(self):
        """Persist task to database - use conn to open a cursor then insert into table
        Replace with an ORM implementation to decouple database schema and object model"""
        return None

    def edit_task(self):
        """Update task description, importance or date in database"""
        return None

    def update_task(self):
        """Mark task as complete or remove"""
        return None

    @classmethod
    def list(cls, conn, completed, subtasks):
        """Class function to list all tasks"""
        return None


class SuperTask(Task):
    def __init__(self, conn, obj):
        super(SuperTask, self).__init__(conn, obj)

    def add_task(self, conn, obj):
        """Persist task to database - use conn to open a cursor then insert into table
        Replace with an ORM implementation to decouple database schema and object model"""
        conn.execute('''INSERT INTO tasks 
                          (description,
                          due_date,
                          high_priority,
                          completed)
                          VALUES 
                          (?, ?, ?, ?)''', (obj.description, obj.due_date, obj.high_priority, obj.completed))
        return True

    def edit_task(self, conn, obj):
        if obj.description is None:
            if obj.high_priority is None:
                conn.execute('''UPDATE tasks
                SET due_date = ?
                WHERE id = ?
                ''', (obj.due_date, obj.id))
            else:
                conn.execute('''UPDATE tasks
                                SET due_date = ?,
                                high_priority = ?
                                WHERE id = ?
                                ''', (obj.due_date, obj.high_priority, obj.id))
        else:
            if obj.high_priority is None:
                conn.execute('''UPDATE tasks
                SET 
                description = ?,
                due_date = ?
                WHERE id = ?
                ''', (obj.description, obj.due_date, obj.id))
            else:
                conn.execute('''UPDATE tasks
                                SET 
                                description = ?,
                                due_date = ?,
                                high_priority = ?
                                WHERE id = ?
                                ''', (obj.description, obj.due_date, obj.high_priority, obj.id))
        return True

    def update_task(self, conn, obj):
        """Mark task as complete or remove"""
        if obj.completed is not None:
            conn.execute('''UPDATE tasks
            SET completed = ?
            WHERE id = ?
            ''', (obj.completed, obj.id))
        if obj.remove is not None:
            conn.execute('''DELETE FROM tasks
            WHERE id = ?
            ''', (obj.id))
        return True

    def list(self, conn, *, task_id=None, list_all=False, completed=False, subtasks=False):
        if task_id is True and list_all is True:
            return f"Can't list all tasks and {task_id} at the same time."
        if task_id is True:
            tasks = conn.execute('''SELECT * FROM tasks WHERE id = ?''', task_id)
            print(task for task in tasks)
            if subtasks is True:
                SubTask.list(task_id, completed)
        elif list_all is True:
            super.list(completed, subtasks)


class SubTask(Task):

    @classmethod
    def list(cls, super_id, completed):
        return None