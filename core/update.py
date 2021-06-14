import os
from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value


def add_parser(sub_parsers: ArgumentParser) -> None:
    blog_init_parser = sub_parsers.add_parser("update")

def main() -> None:
    note_dir = Path(get_config_value("note_dir"))

    os.system(f"cd {note_dir}; git add -A; git commit -m 'pwnbooks.py auto-update'; git push")