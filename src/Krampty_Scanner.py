import ipaddress,os, platform, subprocess, argparse,socket,sys


def list_files_in_dir(directory):
    return os.listdir(directory)