import argparse


def main():
    parser = argparse.ArgumentParser(description="Processes the commands passed to the task app.")

    parser.add_argument("--add",
                        nargs='*',
                        default=argparse.SUPPRESS,
                        help="add a task and completion date",
                        metavar=('<description>', '<date>'),
                        dest='task'
                        )

    parser.add_argument("-p",
                        action='store_true',
                        default=False,
                        help="set as high-priority",
                        dest='high_priority')

    parser.add_argument("--list")

    parser.add_argument("-c")

    parser.add_argument("-a")

    parser.add_argument("-r")

    parser.add_argument("--add-subtask")

    parser.add_argument("--edit")

    parser.add_argument("--update")

    parser.add_argument("--update-subtask")





