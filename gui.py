import FreeSimpleGUI as Sg
import modules.functions as f

label = Sg.Text('Type a to-do')
input_box = Sg.InputText(key='todo',
                         default_text="",
                         tooltip="Enter to-do")
list_box = Sg.Listbox(values=f.get_list_form_file(),
                        key='todolist',
                        enable_events=True,
                        size=[45, 10])
edit_button = Sg.Button('Edit', key='edit_button')
complete_button = Sg.Button('Complete', key='complete_button')
add_button = Sg.Button('Add',
                       key='add_button',
                       tooltip="Add new item")
exit_button = Sg.Button('Exit', key='exit_button')
result = Sg.Text(key='output', text_color='red')
layout=[
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button, result]
]

window = Sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 18))

while True:
    event, values = window.read()
    match event:
        case 'add_button':
            todos = f.get_list_form_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)

            f.update_file(todos)
            window['todolist'].update(values=todos)
        case 'edit_button':
            todo_to_edit = values['todolist'][0]
            new_todo = values['todo'] + '\n'

            todos = f.get_list_form_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            f.update_file(todos)
            window['todolist'].update(values=todos)
        case 'todolist':
            window['todo'].update(value=values['todolist'][0])
        case 'complete_button':
            todo_to_complete = values['todolist'][0]
            todos = f.get_list_form_file()
            todos.remove(todo_to_complete)

            f.update_file(todos)
            window['todo'].update(value='')
            window['todolist'].update(values=todos)
        case 'exit_button':
            exit()
        case Sg.WIN_CLOSED:
            #exit()
            break

window.close()

