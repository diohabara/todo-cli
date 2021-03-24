"""
This module has a TodoApp class
which is an essential part of this cli application
"""


class TaskObject:
    """
    Task information
    """

    def __init__(self, task_name: str, description: str) -> None:
        self.__task_name = task_name
        self.__description = description

    def __eq__(self, other) -> bool:
        if isinstance(self, other.__class__):
            return (self.task_name() is other.task_name()) and (
                self.description() is other.description()
            )
        return False

    def task_name(self) -> str:
        """
        Retrun this object's __task_name
        """
        return self.__task_name

    def description(self) -> str:
        """
        Retrun this object's __description
        """
        return self.__description


class TodoApp:
    """
    Make a __todo cli application.
    """

    def __init__(self) -> None:
        self.__todo: list[TaskObject] = []
        self.__done: list[TaskObject] = []

    def get_todo_tasks(self) -> list[TaskObject]:
        """
        Return all the __todo tasks
        """
        return self.__todo

    def get_done_tasks(self) -> list[TaskObject]:
        """
        Return all the __done tasks
        """
        return self.__done

    def add_task(self, task_name: str, description: str) -> None:
        """
        Add a new task into `self.__todo`.
        """
        self.__todo.append(TaskObject(task_name, description))

    def _add_done(self, task_object: TaskObject) -> None:
        """
        Add a new __done task into `self.__done`.
        """
        self.__done.append(task_object)

    def complete_task(self, task_name: str) -> None:
        """
        Finish a task into `self.__done` as a done task
        """
        for i, task in enumerate(self.__todo):
            if task_name == task.task_name():
                done_task_object = self.__todo.pop(i)
                self._add_done(done_task_object)
                print(f"{done_task_object.task_name} has been done.")
                return
        print(f"Tried to complete {task_name}, but it was not in the todo list")

    def delete_task(self, task_name: str) -> None:
        """
        Delete a task in `self.__todo`
        """
        for i, task in enumerate(self.__todo):
            if task_name == task.task_name():
                done_task_object = self.__todo.pop(i)
                print(f"{done_task_object.task_name} has been done.")
                return
        print(f"Tried to delete {task_name}, but it was not in the todo list")
