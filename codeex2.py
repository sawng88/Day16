import PySimpleGUI as sg
from convert import convert_meter


label1 = sg.Text("Enter feet:")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
result = sg.Text("", key="output")




window = sg.Window('Converter', layout=[[label1,input1],
                                        [label2,input2],
                                        [convert_button,result]])

while True:
    event, values =window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    convert = convert_meter(feet,inches)
    window["output"].update(f"{convert} m")

window.close()