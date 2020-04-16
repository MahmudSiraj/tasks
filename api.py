from datetime import datetime
from collections import namedtuple

# use namedtuple to for records being read in from the database

class Task:
    """Super class for both tasks and subtasks. Constructs a task and provides skeleton CRUD operations."""

    def __init__(self, description, due_date, high_importance, completed):
        self.description = description
        self.due_date = datetime(due_date)  # construct a datetime object to make time deltas and comparisons easier
        self.high_importance = high_importance
        self.completed = completed

    def add_task(self, conn, key, description, due_date, high_importance, completed):
        """Persist task to database - use conn to open a cursor then insert into table
        Replace with an ORM implementation to decouple database schema and object model"""
        return None

    def edit_task(self):
        """Update task description, importance or date in database"""
        return None

    def update_task(self):
        """Mark task as complete or remove"""
        return None


class SuperTask(Task):
    def __init__(self, description, due_date, high_importance, completed):
        super(SuperTask, self).__init__(description, due_date, high_importance, completed)

    def get_id(self):
        return None

    def get_subtasks(self):
        return None

#
# class SubTask(Task):