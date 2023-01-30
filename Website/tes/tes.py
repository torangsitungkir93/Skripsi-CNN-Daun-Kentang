import requests
from PIL import Image
import numpy as np


def ubahRGB():

    png = Image.open(
        "E:\Mata Kuliah\Semester 8\Tugas Akhir\Website\\tes\TrainingHealthy_2.png")
    png.load()  # required for png.split()

    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3])  # 3 is the alpha channel
    background.save('tes.jpg', 'JPEG', quality=80)


ubahRGB()
