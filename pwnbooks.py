#!/usr/bin/python3
import os
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
sub_parsers = parser.add_subparsers(dest="subcommand")


# pwnbooks.py own user <flag>
# pwnbooks.py import /ctf/htb/boxes/blue/nmap/default.nmap (determine file based on extension, use <nmap></nmap> tags in markdown to insert it there)
# pwnbooks.py import passwd -> automatically determine /etc/passwd and put it into codeblock
# pwnbooks.py init blue (maybe --template <type>?)
# pwnbooks.py save

# jarvis.py join htb blue --release --target 10.10.10.210 --pwnbooks (inits pwnbooks for the box)
# jarvis.py pb_own user 83f8e8c38012039daf202
# jarvis.py pb_import nmap/default.nmap 
# jarvis.py pb_change crossfit (changes the pwnbooks context to crossfit [update target if possible?])

# def import_file(path) ---> interface for jarvis.py to import files (default tags to substitue are retrieved from dict in the pwnbooks file maybe?)
# def own(type, flag)
# def init(box_name, ip=None, template=None)
# def change_active_book(box_name)
# def save_changes() ----> push to github repo

#!/usr/bin/python3

import os
import sys
import argparse
import importlib
from pathlib import Path


_MODULE_DICT = {}
parser = argparse.ArgumentParser()
sub_parsers = parser.add_subparsers(dest="subcommand")

def get_script_path():
    return Path(os.path.dirname(os.path.realpath(sys.argv[0])))

def import_modules(folder: str):
	module_dir = get_script_path() / folder
	for module_file in os.listdir(module_dir):
		if ".py" not in module_file:
			continue
		module_name = module_file.split(".")[0]
		module = importlib.import_module(f"{folder}.{module_name}")
		module.add_parser(sub_parsers)
		_MODULE_DICT[module_name] = module.main


# import modules and link parsers
import_modules("core")
import_modules("blog")

subcommand_args = dict(vars(parser.parse_args()))
subcommand = subcommand_args.pop("subcommand", None)

if not subcommand:
	parser.print_help()
	exit(1)

_MODULE_DICT[subcommand](**subcommand_args)