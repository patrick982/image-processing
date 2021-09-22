import os
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

directory = 'input'


def watermark():
    image = Image.open(os.path.join(directory, filename))

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 50)

    width, height = image.size
    draw.text((width - 150, height - 100),
              "Nevolo", (255, 255, 255), font=font)
    plt.subplot(1, 2, 1)
    plt.title("black text")
    image.save(os.path.join(directory, filename))


for filename in os.listdir(directory):
    watermark()
