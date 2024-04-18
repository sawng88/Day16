#import time and date from global moudule 

from functions import get_todos, write_todos
import time


now = time.strftime("%b %d,%Y-%H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add, edit, show , complete or exit:")
    user_action = user_action.strip()

    
    if user_action.startswith("add"):

        todo = user_action[4:] + '\n'
        #Replace the code with "with ...as"
        #file = open('todos.txt','r')
        #todos = file.readlines()
        #file.close()

        todos = get_todos()

        todos.append(todo)
        # replace it with "With.... as"
        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()
        write_todos(todos,"todos.txt")

    elif user_action.startswith("show"):
        
        todos = get_todos("todos.txt")
        
        for index,item in enumerate (todos):
            item = item.strip('\n')
            row = f"{index+1}. {item}"
            print(row)
    
    elif user_action.startswith("edit"):
        try:
            user_edit = int(user_action[5:].strip())
            print(user_edit)
            user_edit = user_edit-1
            

            todos = get_todos()
            
            print('Here is existing todos: ',todos)
            

            new_todo = input("Enter a new todo list: ")
            todos[user_edit] = new_todo + '\n'
            
            write_todos(todos,"todos.txt")
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
        
            user_complete = int(user_action[9:])
            #with get_todos call funtion isn't working in this code
            with open ('todos.txt','r') as file:
                todos = file.readlines()
            index1 = user_complete-1
            todo_to_remove = todos[index1].strip('\n')

            todos.pop(index1)

            write_todos(todos,"todos.txt")
            
            message = f"Todo : , {todo_to_remove},  was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number!")
            continue
    
    
    elif 'exit'in user_action:
        break
    else:
        print("This command is not valid!!")




print ("Congratulation on your todo list!!!!")
print ("Welldone")



