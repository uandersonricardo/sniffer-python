from __future__ import print_function, unicode_literals

import pyshark
from PyInquirer import prompt

from util import get_tshark_interfaces_names, download_image

def main():
    download_image('http://3.bp.blogspot.com/-U8fWJp3DI-s/Xh4YIcnNZOI/AAAAAAAAEPk/Kr3LiwPx5RUFABZiqFFgSfESBYbMix6YQCK4BGAYYCw/s1600/4b832db2-f13d-4aff-88f7-4ed787680f78.jpg')
    return

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