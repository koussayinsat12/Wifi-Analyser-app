import PySimpleGUI as sg
from constants import po1
import graph as g
import sys
import os
def main():
    # Theme ( list of available themes : https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg)
    sg.theme('LightGreen8')
    
    # Components
    layout = [  [[sg.VPush()], sg.Image('wifi.png')],
                [sg.Text('WIFI Doctor', font='Default 26')],

                [[sg.VPush()], sg.Button('ANALYZE', image_data=po1, button_color=('white', sg.theme_background_color()), border_width=0, font='Any 16')],
                
                
                [[sg.VPush()], sg.Text('POWERED BY KG AND AL', font='Default 10')],

                  ]

    window = sg.Window('', layout, element_justification='c', resizable=True, size=(450, 550))

    # Listening for events : Close window + Click on buttons
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event == 'ANALYZE':
            g.graphy()
    window.close()


if __name__ == '__main__':
    main()

