import FreeSimpleGUI as Sg
import modules.functions as f

todos = f.get_list_form_file()
todos = [item.replace('\n','') for item in todos]
print(todos)

label = Sg.Text('Type a to-do')
input_box = Sg.InputText(key='input_box', default_text="", tooltip="Enter to-do")
input_list = Sg.Listbox(values=todos)
add_button = Sg.Button('Add', key='add_button', tooltip="Add new item")

window = Sg.Window('My To-Do App', layout=[
    [label],
    [input_box],
    [input_list],
    [add_button]
])

window.read()
print('Hello')
window.close()

