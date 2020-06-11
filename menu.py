import sys
from task import Task, TaskNotFound
from task_container import TaskContainer

class Menu:
    def __init__(self):
        self.task_container = TaskContainer()
        self.choices = {1: self.add_new_task,
                        2: self.change_task,
                        3: self.delete_task,
                        4: self.search_task,
                        5: self.edit_task_note,
                        6: self.show_all_tasks,
                        7: self.show_task_note,
                        8: self.quit}

    def display_menu(self):
        print("""
1) Add new task
2) Edit a task
3) Delete a task
4) Search a task by matching characters
5) Edit a task note
6) Show all tasks
7) Show note to a task
8) Quit""")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Choose your option: "))
            action = self.choices.get(choice)
            if action:
                action()
            else: (f'{choice} is not a valid choice. Try again')


    def _get_task(self, id):
        task = self.task_container.tasks.get(id)
        return task

    def add_new_task(self):
        task_name = input("Task name: ")
        note = input("Add a note: ")
        task = self.task_container.new_task(task_name, note)
        return task

    def change_task(self):
        id = int(input("Task ID: "))
        new_task_name = input("Edited task: ")
        changed_task = self.task_container.edit_task(id, new_task_name)
        return changed_task

    def delete_task(self):
        id = int(input("Task ID: "))
        self.task_container.del_task(id)

    def search_task(self):
        char = str(input("Type characters to be matched: "))
        matches = self.task_container.search(char)
        for match in matches:
            print(match)

    def edit_task_note(self):
        id = int(input("Task ID: "))
        new_note = input("New note: ")
        self.task_container.edit_note(id, new_note)

    def show_all_tasks(self):
        for id, task in self.task_container.tasks.items():
            print(task.id, '-', task.name)

    def show_task_note(self):
        id = int(input("Task ID: "))
        try:
            task = self._get_task(id)
            print(task.get_note())
            return task.get_note()
        except: pass

    def quit(self):
        sys.exit(0)