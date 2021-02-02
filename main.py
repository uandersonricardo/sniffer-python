from __future__ import print_function, unicode_literals

import pyshark
from PyInquirer import prompt

from util import get_tshark_interfaces_names, download_image

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
    
    capture = pyshark.LiveCapture(interface=answers['interface'], display_filter='http.content_type contains "image"')
    
    for packet in capture.sniff_continuously():
        print("Fazendo download da imagem: " + packet.http.response_for_uri)
        download_image(packet.http.response_for_uri)

if __name__ == "__main__":
    main()