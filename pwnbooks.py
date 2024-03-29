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

def import_module(folder: str):
	module_dir = get_script_path() / folder
	for module_file in os.listdir(module_dir):
		if ".py" not in module_file:
			continue
		module_name = module_file.split(".")[0]
		module = importlib.import_module(f"{folder}.{module_name}")
		module.add_parser(sub_parsers)
		_MODULE_DICT[module_name] = module.main


if __name__ == "__main__":
	# import modules and link parsers
	import_module("core")
	import_module("blog")

	subcommand_args = dict(vars(parser.parse_args()))
	subcommand = subcommand_args.pop("subcommand", None)

	if not subcommand:
		parser.print_help()
		exit(1)

	_MODULE_DICT[subcommand](**subcommand_args)