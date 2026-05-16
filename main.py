from task import TodoApp
from storage import save_tasks, load_tasks
from utils import get_valid_integer, seperator, ask_again, clear_screen
FILENAME = 'data.json'
app = TodoApp() 
def main(): 
    app.tasks = load_tasks(FILENAME) 
    is_first_time = True
    while True: 
        clear_screen()
        if is_first_time:
            app.intro() 
            is_first_time = False
        else: 
            seperator() 
        app.show_option() 
        option = get_valid_integer('What is your option: ') 
        if option == 1: 
            app.add_task() 
            save_tasks(app.tasks,FILENAME) 
        elif option == 2: 
            app.show_task() 
            save_tasks(app.tasks,FILENAME)
        elif option == 3: 
            app.delete_task() 
            save_tasks(app.tasks,FILENAME)
        elif option == 4: 
            app.complete_task() 
            save_tasks(app.tasks,FILENAME)
        elif option == 5: 
            app.search_tasks() 
            save_tasks(app.tasks,FILENAME)
        elif option == 6: 
            app.search_hard_tasks()
            save_tasks(app.tasks,FILENAME)
        elif option == 7: 
            app.search_medium_tasks() 
            save_tasks(app.tasks,FILENAME)
        elif option == 8: 
            app.search_easy_tasks() 
            save_tasks(app.tasks,FILENAME)
        elif option == 9: 
            app.clear() 
            save_tasks(app.tasks,FILENAME)
        elif option == 10: 
            app.greet() 
            return
        else: 
            print('Invalid options!') 
        if ask_again() : 
            continue
        else: 
            app.greet() 
            return
if __name__ == '__main__': 
    main() 