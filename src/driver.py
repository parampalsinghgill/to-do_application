from tasks.task_list import TaskList
from auth import Authenticator


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


def foo(f):
    def new_f():
        print("This is foo function.. decorating zee")
        f()
    return new_f


@foo
def zee():
    print("This is zee function")


def outer(x):
    def inner(y):
        return x + y
    return inner

def test_auth():
    auth = Authenticator()
    auth.signup("parampal", "psg@gmail.com", "abc@1")
    auth.signup("gill", "psg@gmail.com", "abc@1")

    auth.login("parampal", "abc@1")



if __name__ == "__main__":
    # execute()
    # zee()
    # print(outer(5)(6))
    test_auth()

