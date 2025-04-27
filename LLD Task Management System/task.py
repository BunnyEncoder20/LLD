from enum import Enum
from datetime import datetime


class TaskStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    
class Task:
    def __init__(self, task_id, title, desc, due_date, priority, assigned_user):
        self.id = task_id
        self.title = title
        self.desc = desc
        self.due_date = due_date
        self.priority = priority
        self.status = TaskStatus.PENDING
        self.assigned_user = assigned_user
    
    def __str__(self):
        return f"[{self.id}] | [{self.priority}]: {self.title} - {self.desc} | {self.due_date} | Assigned:{self.assigned_user} | Status: {self.status}"
        
    # Getter and setters
    def get_id(self): return self.id
    def get_title(self): return self.title
    def get_desc(self): return self.desc
    def get_priority(self): return self.priority
    def get_due_date(self): return self.due_date
    def get_status(self): return self.status
    def get_assigned_user(self): return self.assigned_user
    
    def set_title(self, title): self.title = title
    def set_desc(self, desc): self.title = desc
    def set_due_date(self, due_date): self.due_date = due_date
    def set_priority(self, priority): self.priority = priority
    def set_status(self, status): self.status = status
