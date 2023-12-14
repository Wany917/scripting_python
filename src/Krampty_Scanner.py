import ipaddress,os, platform, subprocess, argparse,socket,sys


def list_files_in_dir(directory):
    return os.listdir(directory)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
      
    return os.listdir(directory)


def display_interface():
    interfaces = get_network_interfaces()
    for interface, details in interfaces.items():
        print(f"Interface: {interface}")
        for key, value in details.items():
            print(f" {key}: {value}")
        print()