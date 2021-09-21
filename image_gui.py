
import warnings
import PySimpleGUI as sg
import os
from PIL import Image, ImageEnhance

sg.theme('Dark Grey 5')  # please make your creations colorful

# ------ Menu Definition ------ #
menu_def = [['File', ['Exit', 'Properties']],
            ['Help', 'About...'], ]

layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Text('Input Folder')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Text('Output Folder')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.OK(), sg.Cancel()]]


window = sg.Window('Automatic Underwater Image Postprocessing', layout)
event, values = window.read()

# Menu Loop WIP
"""
while True:
    event, values = window.read()
    # print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'About...':
        sg.popup('About this program:', 'Automatic Underwater Image Postprocessing', 'Version 1.0',
                 'Author: Patrick Stampler')
"""

input_path = values["Browse"]
output_path = values["Browse0"]


# test if path value could be read in
# print(path)

directory = input_path

try:
    for filename in os.listdir(directory):
        file_name, file_extension = os.path.splitext(filename)

        if file_extension == ".png" or file_extension == ".jpeg" or file_extension == ".jpg":
            # print(file_extension)
            image = Image.open(os.path.join(directory, filename))
            # success check
            # image.show()
            # enhancing the contrast
            contrast = ImageEnhance.Contrast(image)
            image = contrast.enhance(1.5)

            # enhancing color
            color = ImageEnhance.Color(image)
            image = color.enhance(1.5)

            # hue shifts
            color = Image.new('RGB', image.size, 'red')
            image = Image.blend(image, color, 0.1)

            color = Image.new('RGB', image.size, 'yellow')
            image = Image.blend(image, color, 0.001)

            color = Image.new('RGB', image.size, 'blue')
            image = Image.blend(image, color, -0.001)

            # enhancing brightness
            color = ImageEnhance.Brightness(image)
            image = color.enhance(1.2)

            # enhancing sharpness
            color = ImageEnhance.Sharpness(image)
            image = color.enhance(1.5)

            # save the result
            image.save(os.path.join(output_path, filename))
        else:
            print("No .png, or .jpeg, or .jpg File found :(")

except:
    sg.popup_error("Filepaths cannot be empty!")

window.close()
