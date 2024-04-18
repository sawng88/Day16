import PySimpleGUI as sg

label1 = sg.Text("Enter Feet:")
input1 = sg.Input()

label2 = sg.Text("Enter Inches:")
input2 = sg.Input()

Convert_button = sg.Button("Convert")

Window = sg.Window("Convertor", layout=[[label1,input1],
                                        [label2, input2],
                                        [Convert_button]])

Window.read()
Window.close()