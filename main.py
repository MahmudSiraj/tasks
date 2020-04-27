import argparse
import sqlite3
from api import *


class Task(NamedTuple):
    id: int
    description: str
    due_date: datetime
    high_priority: bool
    completed: bool


class SubTask(NamedTuple):
    id: int
    task_id: int
    description: str
    due_date: datetime
    high_priority: bool
    completed: bool




def main():

    # database connection
    conn_tasks = sqlite3.Connection("tasks.db")
    conn_subtasks = sqlite3.Connection("subtasks.db")

    parser = argparse.ArgumentParser(description="Processes the commands passed to the task app.")

    subparsers = parser.add_subparsers()

    subparser_add = subparsers.add_parser('add')

    subparser_add.add_argument(nargs='+',
                               default=[],
                               help="add a task and completion date",
                               metavar=('[<task_id>], <description>', '<date>'),
                               dest='task'
                               )

    subparser_add.add_argument("-p",
                               action="store_true",
                               default=False,
                               help="set as high-priority",
                               dest='high_priority')

    subparser_add.add_argument("-s", "--subtask",
                               action="store_true",
                               default=False,
                               help="set as a subtask",
                               dest='subtask')

    subparser_list = subparsers.add_parser('list')

    subparser_list.add_argument(nargs='?',
                                default=argparse.SUPPRESS,
                                help='list the tasks',
                                metavar="<task_id>",
                                dest="task")

    subparser_list.add_argument('-a', '--all',
                                action='store_true',
                                default=False,
                                help='list all the tasks',
                                dest="list_all")

    subparser_list.add_argument('-c', '--completed',
                                action='store_true',
                                default=False,
                                help='list only completed tasks',
                                dest="list_completed")

    subparser_list.add_argument('-s', '--subtasks',
                                action='store_true',
                                default=False,
                                help='list subtasks too',
                                dest="list_subtasks")

    subparser_edit = subparsers.add_parser('edit')

    subparser_edit.add_argument(nargs='+',
                                default=argparse.SUPPRESS,
                                help='edit a task',
                                metavar=('<task_id>', '<description>', '<date>'),
                                dest="task")

    subparser_edit.add_argument("-p",
                                action="store_true",
                                default=False,
                                help="set as high-priority",
                                dest='high_priority')

    subparser_edit.add_argument("-s", "--subtask",
                                action="store_true",
                                default=False,
                                help="mark as subtask",
                                dest='subtask')

    subparser_update = subparsers.add_parser('update')

    subparser_update.add_argument(nargs='1',
                                  default=argparse.SUPPRESS,
                                  help='update a task',
                                  metavar='<task_id>',
                                  dest="task")

    subparser_update.add_argument("-s", "--subtask",
                                  action="store_true",
                                  default=False,
                                  help="mark as subtask",
                                  dest='subtask')

    subparser_update.add_argument("-c", "--complete",
                                  action="store_true",
                                  default=False,
                                  help="mark as complete",
                                  dest='complete')

    subparser_update.add_argument("-r", "--remove",
                                  action="store_true",
                                  default=False,
                                  help="remove task",
                                  dest='remove')
