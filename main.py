from __future__ import print_function, unicode_literals
import pyshark
import os
import subprocess

from pprint import pprint
from pyshark.tshark.tshark import get_process_path
from PyInquirer import prompt, Separator, style_from_dict

def get_interface_name_from_line(line):
    name = line.split("(")[1]
    return name[:-1]

def get_tshark_interfaces_names(tshark_path=None):
    parameters = [get_process_path(tshark_path), "-D"]
    with open(os.devnull, "w") as null:
        tshark_interfaces = subprocess.check_output(parameters, stderr=null).decode("utf-8")

    return [get_interface_name_from_line(line) for line in tshark_interfaces.splitlines() if not '\\\\.\\' in line]

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

    capture = pyshark.LiveCapture(interface=answers['interface'])

    for packet in capture.sniff_continuously():
        print('Just arrived:', packet)

if __name__ == "__main__":
    main()