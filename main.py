#from functions import  get_list_form_file, update_file
from modules import functions as f

while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    # Get user input and remove space chars from it
    user_action = user_action.strip().lower()

    if user_action.startswith('add '):
        # get substring from char 4
        todo = user_action[4:] + "\n"
        try:
            todos = f.get_list_form_file()

            todos.append(todo)
            f.update_file(todos)
        except Exception as e:
            exception_message = str(e)
            print(f"An error occurred: {exception_message}")

    elif user_action.startswith("show"):
        todos = f.get_list_form_file()

        # stripped_todos = [item.strip('\n').title() for item in todos]

        for index, item in enumerate(todos):
            print(f"{index} - {item.strip('\n').title()}")
    elif user_action.startswith("edit"):
        todos = f.get_list_form_file()
        try:
            index = int(user_action[5:])
            new_value = input("Enter a new value: ")
            todos[index] = new_value + "\n"

            f.update_file(list_todos=todos)
        except IndexError:
            print("Command is not valid")
            continue
    elif user_action.startswith("complete"):
        todos = f.get_list_form_file()
        try:
            index = int(user_action[9:])
            todos.pop(index)
            f.update_file(todos)
            print(f"Todo {index} was completed and removed from the list")
        except IndexError:
            print("Command is not valid")
            continue
    elif user_action.startswith("exit") or user_action.startswith("quit"):
        break
    else :
        print("Hey, you entered unknown command")




