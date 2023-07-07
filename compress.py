import PySimpleGUI as sg
from zip_creator import make_archive

sg.theme("Purple")

label1 = sg.Text("Select the files to compress ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select the destination folder ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label=sg.Text(key="output")
window = sg.Window("File-Zipper🤐",
                   layout=[[label1, input1, choose_button1]
                       , [label2, input2, choose_button2]
                       , [compress_button,output_label]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed",text_color="green")


    match event:
        case sg.WIN_CLOSED:
            break

window.close()
