import FreeSimpleGUI as Sg
import modules.functions as f

#todos = f.get_list_form_file()
#todos_to_show = [item.replace('\n','') for item in todos]

label = Sg.Text('Type a to-do')
input_box = Sg.InputText(key='todo', default_text="", tooltip="Enter to-do")
#input_list = Sg.Listbox(values=todos_to_show)
add_button = Sg.Button('Add', key='add_button', tooltip="Add new item")

window = Sg.Window('My To-Do App',
                   layout=[
    [label],
    [input_box],
    #[input_list],
    [add_button]
],
                   font=('Helvetica', 18))

while True:
    event, values = window.read()
    print(event)
    print(values['todo'])
    match event:
        case 'add_button':
            todos = f.get_list_form_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            f.update_file(todos)
        case Sg.WIN_CLOSED:
            break

window.close()

