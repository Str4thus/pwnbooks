import os
from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value


def add_parser(sub_parsers: ArgumentParser) -> None:
    sub_parsers.add_parser("blog_update")

def main() -> None:
    blog_dir = Path(get_config_value("blog_dir"))

    os.system(f"cd {blog_dir}; git add -A; git commit -m 'pwnbooks.py auto-update'; git push")