"""
Test the todo cli application
"""
from todo_cli.todo_app import TaskObject, TodoApp


def test_add_tasks():
    app = TodoApp()
    app.add_task("taskA", "1")
    app.add_task("taskB", "2")
    assert len(app.get_todo_tasks()) == 2
    app.add_task("taskC", "3")
    assert len(app.get_todo_tasks()) == 3


def test_complete_task():
    app = TodoApp()
    app.add_task("taskA", "1")
    app.add_task("taskB", "2")
    assert len(app.get_todo_tasks()) == 2

    app.complete_task("taskA")
    assert len(app.get_todo_tasks()) == 1
    assert len(app.get_done_tasks()) == 1
    assert app.get_done_tasks()[0] == TaskObject("taskA", "1")

    app.complete_task("taskB")
    assert len(app.get_todo_tasks()) == 0
    assert len(app.get_done_tasks()) == 2
    assert app.get_done_tasks()[0] == TaskObject("taskA", "1")
    assert app.get_done_tasks()[1] == TaskObject("taskB", "2")

    app.complete_task("taskC")
    assert len(app.get_done_tasks()) == 2


def test_delete_tasks():
    app = TodoApp()
    app.add_task("taskA", "1")
    app.add_task("taskB", "2")
    app.add_task("taskC", "3")
    assert len(app.get_todo_tasks()) == 3

    app.delete_task("taskC")
    assert len(app.get_todo_tasks()) == 2
    app.delete_task("taskB")
    app.delete_task("taskA")
    assert len(app.get_todo_tasks()) == 0

    app.delete_task("taskA")
    assert len(app.get_todo_tasks()) == 0


if __name__ == "__main__":
    test_add_tasks()
