from __future__ import print_function, unicode_literals

import pyshark
from PyInquirer import prompt

from util import get_tshark_interfaces_names, download_image
from image_capture import ImageCapture

def main():
    questions = [
        {
            'type': 'list',
            'name': 'interface',
            'message': 'Deseja capturar os pacotes de qual interface?',
            'choices': get_tshark_interfaces_names()
        }
    ]

    answers = prompt(questions)
    
    capture = ImageCapture(interface=answers['interface'])
    
    for image_uri in capture.sniff_continuously():
        print("Fazendo download da imagem: " + image_uri)
        download_image(image_uri)

if __name__ == "__main__":
    main()