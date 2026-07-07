
import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r" , encoding="utf-8") as f:
            tasks=json.load(f)
            
        return tasks
    else:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w",encoding="utf-8") as f:
        json.dump(tasks,f,ensure_ascii=False,indent=4)
        
def add_task(tasks):
    task_name=input("new task i elave et")
    new_task={"title": task_name,"done":False}
    tasks.append(new_task)
        
def show_tasks(tasks):
    if len(tasks)==0:
        print("task yoxdu")
        
    else:
        for index, task in enumerate(tasks,start=1):
            if task["done"]:
                status="bitib"
                
            else :
                status="bitmiyib"
        
            print(f"{index} . {task['title']} - {status}")
            
def delete_task(tasks):
    show_tasks(tasks)
    number=int(input("silmek istediyimiz nomreli task"))
    index=number-1
    del tasks[index]
    
def complete_task(tasks):
    show_tasks(tasks)
    number=int(input("complete elemek istediyimiz task"))
    index=number-1
    tasks[index]["done"]=True
    

tasks=load_tasks()

while True :
    print("1. add ele")
    print("2. show ele")
    print("3. delete  ele")
    print("4. complete ele")
    print("5.  cix")
    
    choice=int(input("secimi daxil ele"))
    
    if choice==1:
        add_task(tasks)
        save_tasks(tasks)
    elif choice==2:
        show_tasks(tasks)
    elif choice==3:
        delete_task(tasks)
        save_tasks(tasks)
    elif choice==4:
        complete_task(tasks)
        save_tasks(tasks)
    elif choice==5:
        print("cixilir....")
        break
    else :
        print("secimi yeniden daxil ele")
            
    
    
    
    