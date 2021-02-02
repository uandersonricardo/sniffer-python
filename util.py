import os
import subprocess

from pyshark.tshark.tshark import get_process_path

def get_interface_name_from_line(line):
    name = line.split("(")[1]
    return name[:-1]

def get_tshark_interfaces_names(tshark_path=None):
    parameters = [get_process_path(tshark_path), "-D"]
    with open(os.devnull, "w") as null:
        tshark_interfaces = subprocess.check_output(parameters, stderr=null).decode("utf-8")

    return [get_interface_name_from_line(line) for line in tshark_interfaces.splitlines() if not '\\\\.\\' in line]