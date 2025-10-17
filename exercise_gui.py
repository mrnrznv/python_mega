import FreeSimpleGUI as sg
import modules.zip_creator as zip_creator

"""
label1 = sg.Text('Select files to compress: ', font=('Arial', 16))
input1 = sg.Input(key='files', enable_events=True)
button1 = sg.FilesBrowse('Choose', key='files_choose')

label2 = sg.Text('Select destination folder: ', font=('Arial', 16))
input2 = sg.Input(key='folder', enable_events=True)
button2 = sg.FolderBrowse('Choose', key='folder_select')

button = sg.Button('Compress', key='compress')
output = sg.Text(key='output', text_color='green')

layout = [
    [label1, input1, button1],
    [label2, input2, button2],
    [button],
    [output]
]

window = sg.Window('File Compressor',
                   layout=layout)

window.read()

while True:
    event, values = window.read()
    filepaths = values['files'].split(';')
    folder = values['folder']
    match event:
        case 'compress':
            zip_creator.make_zip(filepaths, folder)
            window['output'].update(value='Compression Complete')
        case sg.WIN_CLOSED:
            break

window.close()
"""

"""

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                            [option2],
                            [option3],
                            [option4],
                           ])

window.read()
window.close()

"""
"""
import modules.exercise_functions as f

label1 = sg.Text("Enter feet")
input1 = sg.Input(key='feet', enable_events=True)

label2 = sg.Text("Enter inches")
input2 = sg.Input(key='inches', enable_events=True)

result_button = sg.Button('Convert', key='convert')

result = sg.Text(key='output', text_color='blue')

layout = [[label1, input1],
          [label2, input2],
          [result_button],
          [result],]
window = sg.Window('File Compressor',
                   layout=layout)

window.read()

while True:
    event, values = window.read()
    match event:
        case 'convert':
           feet = int(values['feet'])
           inches = int(values['inches'])
           result = f.convert(feet, inches)
           window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()

"""