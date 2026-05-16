import os
import datetime
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear') 
def format_datetime(): 
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def validate_levels(level:str): 
    levels = ['easy','medium','hard'] 
    return level.lower().strip() in levels
def get_valid_integer(message): 
    while True: 
        try: 
            return int(input(message)) 
        except ValueError: 
            print('Invalid input!') 
def normalize_text(text:str): 
    return text.lower().strip() 
def seperator(): 
    print('----***----') 
def ask_again(): 
    again = input('Do you want to continue using our app(yes/no):').lower().strip()
    return again == 'yes'