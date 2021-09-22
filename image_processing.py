
import os
from PIL import Image, ImageEnhance

# packing the whole post processing into a function


def image_processing():
    directory = 'input'

    for filename in os.listdir(directory):

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
        image.save(os.path.join('output', filename))


# calling that function

image_processing()
