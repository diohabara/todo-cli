"""
This script prompts a user to enter what this app will next.
"""
from todo_cli.todo_app import TodoApp


def display_current_todo_tasks(current_app: TodoApp) -> None:
    """
    Display todo tasks that `current_app` has
    """
    print(
        "These are the TODO tasks you have: ",
        [
            f"{todo.task_name()}: {todo.description()}"
            for todo in current_app.get_todo_tasks()
        ],
        sep="\n",
    )


def display_current_done_tasks(current_app: TodoApp) -> None:
    """
    Display done tasks that `current_app` has
    """
    print(
        "These are the DONE tasks you have: ",
        [
            f"{todo.task_name()}: {todo.description()}"
            for todo in current_app.get_done_tasks()
        ],
        sep="\n",
    )


if __name__ == "__main__":
    app = TodoApp()
    while True:
        option = input(
            """
            Please enter want you want to do:
            [a]dd
            [c]omplete
            [d]elete
            [l]ist
            """
        )

        if option in ("a", "add"):
            task_name = input("What is the task name?> ")
            description = input("Can you describe the task?> ")
            app.add_task(task_name, description)

        elif option in ("c", "complete"):
            display_current_todo_tasks(app)
            task_name = input("What task have you completed?")
            app.complete_task(task_name)

        elif option in ("d", "delete"):
            display_current_todo_tasks(app)
            task_name = input("What task do you want to delete?")
            app.delete_task(task_name)

        elif option in ("l", "list"):
            display_current_todo_tasks(app)
            display_current_done_tasks(app)
        else:
            print("This option is not implemented")
