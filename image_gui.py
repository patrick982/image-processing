
import warnings
import PySimpleGUI as sg
import os
from PIL import Image, ImageEnhance
from PySimpleGUI.PySimpleGUI import popup, popup_error, popup_notify, popup_ok, popup_quick_message


def image_processing():
    # event, values = window.read()
    input_path = values["Browse"]
    output_path = values["Browse0"]
    contrast_setting = float(values["contrast_slider"])
    color_setting = float(values["color_slider"])
    red_setting = float(values["red_slider"])
    yellow_setting = float(values["yellow_slider"])

    directory = input_path
    out_directory = output_path
    totalFiles = 0
    file_count = 0

    # count files in directory
    for filename in os.listdir(directory):
        totalFiles = totalFiles + 1

    for filename in os.listdir(directory):
        file_name, file_extension = os.path.splitext(filename)
        file_count = file_count + 1

        if file_extension == ".png" or file_extension == ".jpeg" or file_extension == ".jpg":
            # print(file_extension)
            image = Image.open(os.path.join(directory, filename))
            # success check
            # image.show()

            # enhancing the contrast
            contrast = ImageEnhance.Contrast(image)
            image = contrast.enhance(contrast_setting)

            # enhancing color
            color = ImageEnhance.Color(image)
            image = color.enhance(color_setting)

            # hue shifts
            color = Image.new('RGB', image.size, 'red')
            image = Image.blend(image, color, red_setting)

            # color = Image.new('RGB', image.size, 'yellow')
            # image = Image.blend(image, color, 0.001)

            # color = Image.new('RGB', image.size, 'blue')
            # image = Image.blend(image, color, -0.001)

            # enhancing brightness
            # color = ImageEnhance.Brightness(image)
            # image = color.enhance(1.2)

            # enhancing sharpness
            # color = ImageEnhance.Sharpness(image)
            # image = color.enhance(1.5)

            popup_quick_message(
                "processing - please wait  " + str(file_count) + " / " + str(totalFiles))

            # save the result
            image.save(os.path.join(out_directory, filename))

    else:
        print("No .png, or .jpeg, or .jpg File found :(")


# please make your creations colorful
sg.theme('Dark Grey 14')

# ------ Menu Definition ------ #
menu_def = [['File', ['Exit']],
            ['Help', 'About...'], ]

layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Text('Input Folder')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Text('Output Folder')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Text('Contrast')],
          [sg.Slider((1, 2), default_value=1.2, resolution=.01, key="contrast_slider", orientation="h",
                     enable_events=True)],
          [sg.Text('Color Correction')],
          [sg.Slider((1, 2), default_value=1.1, resolution=.01, key="color_slider", orientation="h",
                     enable_events=True)],
          [sg.Text('Red')],
          [sg.Slider((0, 1), default_value=0.10, resolution=.01, key="red_slider", orientation="h",
                     enable_events=True)],
          [sg.Text('Yellow')],
          [sg.Slider((0, 1), default_value=0.10, resolution=.01, key="yellow_slider", orientation="h",
           enable_events=True)],
          [sg.OK("Process"), sg.Button("Watermark"), sg.Exit()]]

window = sg.Window('Automatic Underwater Image Postprocessing', layout)


# Program Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'About...':
        sg.popup('About this program:', 'Automatic Underwater Image Postprocessing', 'Version 1.0',
                 'Author: Patrick Stampler')
    elif event == 'Watermark':
        popup_ok("Feature not ready..")
    elif event == 'Process':

        # disable all buttons during process
        window["Process"].update(disabled=True)
        window["Watermark"].update(disabled=True)
        window["Exit"].update(disabled=True)
        window["Browse0"].update(disabled=True)
        window["Browse"].update(disabled=True)
        event, values = window.read(timeout=1)

        try:
            image_processing()
        except:
            popup_error("Filepath empty!")

        popup_ok("done")

        # enable buttons again
        window["Process"].update(disabled=False)
        window["Watermark"].update(disabled=False)
        window["Exit"].update(disabled=False)
        window["Browse0"].update(disabled=False)
        window["Browse"].update(disabled=False)
