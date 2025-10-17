import FreeSimpleGUI as sg

"""
label1 = sg.Text('Select files to compress: ', font=('Arial', 16))
input1 = sg.Input()
button1 = sg.FilesBrowse('Choose')

label2 = sg.Text('Select destination folder: ', font=('Arial', 16))
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

button = sg.Button('Compress')

layout = [
    [label1, input1, button1],
    [label2, input2, button2],
    [button]
]

window = sg.Window('File Compressor',
                   layout=layout)

window.read()
window.close()

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