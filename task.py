
from utils import normalize_text, format_datetime, validate_levels
class TodoApp:
    def __init__(self) : 
        self.tasks = []  
    def show_option(self): 
        print('Options')
        print('1.Add task') 
        print('2.View task') 
        print('3.Delete task') 
        print('4.Complete task') 
        print('5.Search task') 
        print('6.Search Hard Tasks')
        print('7.Search Medium Tasks')
        print('8.Search Easy Tasks') 
        print('9.Empty your list') 
        print('10.Exit') 
    def add_task (self) : 
        task_name = input('What is your task: ').strip()  
        task_level = input('What is its level (easy,medium,hard): ').strip() 
        if validate_levels(task_level): 
            self.tasks.append(
                {
                    'name': task_name, 
                    'completed': False, 
                    'created_at': format_datetime(),
                    'level': task_level
                }
        ) 
        else: 
            print('Invalid level!') 
        print(f'Your task is successfully added!') 
    def show_task (self) : 
        if not self.tasks: 
            print('Your list is empty.') 
            return
        print('---Easy---')
        k = 1
        for task in self.tasks: 
            if task['level'].lower() == 'easy': 
                print(f'{k}. {task['name']}')
                k += 1 
        print('---Medium---')
        j = 1
        for task in self.tasks: 
            if task['level'].lower() == 'medium': 
                print(f'{j}. {task['name']}') 
                j += 1
        print('---Hard---')
        i = 1
        for task in self.tasks: 
            if task['level'].lower() == 'hard': 
                print(f'{i}. {task['name']}') 
                i += 1
    def delete_task (self) : 
        for index, task in enumerate(self.tasks): 
            print(f'{index+1}. {task['name']}') 
        option = int(input('What task would you like to delete: '))
        if option > 0 and option <= len(self.tasks): 
            task_name = self.tasks[option-1]['name'] 
            del self.tasks[option-1] 
            print(f'{task_name} is successfully deleted from your list!') 
        else: 
            print(f'Invalid option!')  
    def complete_task(self) : 
        for index, task in enumerate(self.tasks): 
            print(f'{index+1}. {task['name']}') 
        option = int(input('What task have you completed: ')) 
        if option > 0 and option <= len(self.tasks):
            task_name = self.tasks[option-1]['name'] 
            self.tasks[option-1]['completed'] = True
            print(f'{task_name} is completed!') 
        else: 
            print('Invalid option!') 
    def search_tasks(self): 
        keyword = normalize_text(input('Search: ')) 
        keywords = keyword.split() 
        found = False
        for i, task in enumerate(self.tasks,start=1): 
            task_name = task['name'].lower()   
            score = 0
            for keyword in keywords: 
                if keyword in task_name: 
                    score += 1
            if score >= 1: 
                print(f'{i}. {task_name}') 
                found = True
        if not found: 
            print('No watching tasks found!') 
    def search_hard_tasks(self): 
        print('---Hard Tasks---')
        i = 1
        for task in self.tasks: 
            if task['level'].lower() == 'hard': 
                print(f'{i}. {task['name']}')
                i += 1
        if i == 1: 
            print('Sorry! We could not find any hard tasks.')
    def search_medium_tasks(self): 
        print('---Medium Tasks---')
        i = 1
        for task in self.tasks: 
            if task['level'].lower() == 'medium': 
                print(f'{i}. {task['name']}')
                i += 1
        if i == 1: 
            print('Sorry! We could not find any medium tasks.') 
    def search_easy_tasks(self): 
        print('---Easy Tasks---')
        i = 1
        for task in self.tasks: 
            if task['level'].lower() == 'easy': 
                print(f'{i}. {task['name']}')
                i += 1
        if i == 1: 
            print('Sorry! We could not find any easy tasks.')       
    def clear(self): 
        self.tasks.clear() 
        print('Your list is empty now!') 
    def greet (self) : 
        print('Thanks for using our app!')
    def intro (self) : 
        print('===CLI TODO APP===') 
        print('Welcome to our app!') 
        print('This is where you can organize your daily task!')