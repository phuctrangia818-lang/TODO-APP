import json 
def save_tasks(object:list,filename:str) -> None: 
    with open(filename,'w',encoding='utf-8') as file: 
        json.dump(object,file) 
def load_tasks(filename:str) -> list: 
    with open(filename,'r',encoding='utf-8') as file: 
        return json.load(file) 