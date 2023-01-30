import requests
from PIL import Image
import numpy as np


def removeBg(img):

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'QE4uquU353XdUPpX57xsAudB'},
    )
    if response.status_code == requests.codes.ok:
        with open('no_bgUploadedFile.png', 'wb') as out:
            out.write(response.content)
        return True
    else:
        print("Error:", response.status_code, response.text)
        return False


def ubahRGB():

    png = Image.open(
        "E:\Mata Kuliah\Semester 8\Tugas Akhir\Website\\no_bgUploadedFile.png")
    png.load()  # required for png.split()

    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3])  # 3 is the alpha channel

    background.save('out.jpg', 'JPEG', quality=80)
