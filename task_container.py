from task import Task, TaskNotFound
import re

class TaskContainer:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task_name, note=None):
        task = Task(task_name, note)
        self.tasks.update({task.id:task})
        return task

    def _is_valid_id(self, id):
        if id in self.tasks.keys(): return True
        return False

    def _get_task_by_id(self, id):
        return self.tasks.get(id)

    def edit_task(self, id, task_name):
        if not self._is_valid_id(id): raise TaskNotFound
        task = self._get_task_by_id(id)
        task.name = task_name
        return task

    def del_task(self, id):
        if not self._is_valid_id(id): raise TaskNotFound
        del self.tasks[id]

    def search(self, char):
        matches = [task.name for task in self.tasks.values() if re.search(char, task.name, re.I)]
        return matches

    def edit_note(self, id, new_note):
        if not self._is_valid_id(id): raise TaskNotFound
        task = self._get_task_by_id(id)
        task.change_note(new_note)

    def get_task_note(self, id):
        if not self._is_valid_id(id): raise TaskNotFound
        task = self._get_task_by_id(id)
        return task.get_note()