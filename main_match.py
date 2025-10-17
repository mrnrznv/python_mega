file_path = "files/todos.txt"
absolute_path = r"C:\Users\mrnrznv\Documents\python-mega-course\to-do-list\files\todos.txt"

def get_list_form_file(filename, mode):
    with open(filename, mode) as file:
        list_todos = file.readlines()

    return list_todos

def update_file(filename, mode, list_todos):
    with open(filename, mode) as file:
        file.writelines(list_todos)

while True:
    user_action = input("Type add, edit, show, complete or quit: ")
    # Get user input and remove space chars from it
    match user_action.strip().lower():
        case "add" | "append":
            todo = input("Enter todo: ") + "\n"

            todos = get_list_form_file(file_path, "r")
            todos.append(todo)

            update_file(file_path, "w", todos)
        case "show" | "display":
            todos = get_list_form_file(file_path, "r")

            # stripped_todos = [item.strip('\n').title() for item in todos]

            for index, item in enumerate(todos):
                print(f"{index} - {item.strip('\n').title()}")
        case "edit":
            todos = get_list_form_file(file_path, "r")

            index = input("Enter index of item to edit: ")
            index = int(index)
            if index > len(todos):
                print(f"Index {index} is greater than the length of todos")
            else:
                new_value = input("Enter a new value: ")
                todos[index] = new_value + "\n"

                update_file(file_path, "w", todos)
        case "complete":
            todos = get_list_form_file(file_path, "r")

            number = int(input("Enter index of the todo item to complete: "))
            if number > len(todos):
                print(f"Index {number} is greater than the length of todos")
            else:
                todos.pop(number)
                update_file(file_path, "w", todos)
                print(f"Todo {number} was completed and removed from the list")

        case "q" | "quit" | "exit":
            break
        case _:
            print("Hey, you entered unknown command")




