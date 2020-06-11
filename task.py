from note import Note

class Task:
    id = 1
    def __init__(self, name, note=None):
        self.name = name
        self.message = Note(note) if note is not None else None
        self.id = Task.id
        Task.id += 1

    def get_task_name(self):
        return f'{self.name}'

    def get_note(self):
        return f'{self.message}'

    def change_note(self, new_message):
        self.message = Note(new_message)
        return f'{self.message.note}'

    def match(self, word):
        if word in self.name: return True
        return False

class TaskNotFound(Exception):
    pass