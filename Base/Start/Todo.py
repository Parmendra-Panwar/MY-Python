todo = []

def addToDo(task):
    todo.append(task)
    print(f"Added: {task}")

def deleteToDo(task):
    if task in todo:
        todo.remove(task)
        print(f"Removed: {task}")
    else:
        print("Task not found.")

def runToDo():
    while True:
        print("\nCurrent Todo List:", todo)
        print('0: Add task | 1: Remove task | 2: Exit')
        
        choice = input('Enter choice: ')
        
        if choice == '0':
            task = input('Enter task to add: ')
            addToDo(task)
        elif choice == '1':
            task = input('Enter task to remove: ')
            deleteToDo(task)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

runToDo()