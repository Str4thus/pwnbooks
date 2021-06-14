import os
from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value


def add_parser(sub_parsers: ArgumentParser) -> None:
    blog_init_parser = sub_parsers.add_parser("blog_update")

def main() -> None:
    blog_dir = Path(get_config_value("blog_dir"))

    os.system(f"cd {blog_dir}")
    os.system("git add -A")
    os.system("git commit -m 'pwnbooks.py auto-update'")
    os.system("git push")