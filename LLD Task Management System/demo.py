from task_manager import TaskManager
from task import Task, TaskStatus
from user import User
from datetime import datetime

class TaskManagerSystem_demo:
    @staticmethod
    def run():
        # init the system
        task_manager = TaskManager.get_instance()
        
        # make users
        user1 = User("1", "Varun Verma", "varun.verma2024@gmail.com")
        user2 = User("2", "Soma Senpai", "soma.senpai2024@gmail.com")
        
        # create tasks
        task1 = Task("1", "Task 1", "check bike coolant", datetime.now(), 1, user1)
        task2 = Task("2", "Task 2", "check bike brakes", datetime.now(), 2, user2)
        task3 = Task("3", "Task 3", "repair bike clutch wire", datetime.now(), 1, user2)

        # add task to Task manager
        task_manager.create_task(task1)
        task_manager.create_task(task2)
        task_manager.create_task(task3)
        
        # update a task
        task2.set_description("repair indicators")
        task_manager.update_task(task2)
        
        # search tasks
        search_results = task_manager.search_tasks("Task")
        print("Search Results:")
        for task in search_results:
            print(task.get_title())
        
        # filter tasks
        filtered_tasks = task_manager.filter_tasks(TaskStatus.Pending, datetime(1970, 1, 1), datetime.now(), 1)
        print("Filtered Tasks:")
        for task in filtered_tasks:
            print(task.get_title())

        # Mark a task as completed
        task_manager.mark_completed("1")

        # get task history for user 
        task_history = task_manager.get_task_history(user1)
        print(f"Task history for {user1.get_name()} :")
        for task in task_history:
            print(task.get_title())
        
        # delete task
        task_manager.delete_task("3")
    
if __name__ == "__main__":
    TaskManagerSystem_demo.run()
