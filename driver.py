from task_list import TaskList


def execute():
    tl = TaskList()
    tl.create_task("work", 2)
    tl.create_task("play", 3)
    tl.create_task("learn", 2)
    tl.create_task("apply", 5)
    tl.create_task("work hard", 5)

    tl.print_tasks()

    tl.modify_task(1, "work on python project")
    tl.search("work")
    tl.delete_task(3)


if __name__ == "__main__":
    execute()
