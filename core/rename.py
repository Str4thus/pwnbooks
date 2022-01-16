import os
from pathlib import Path
from .config import get_config_value, set_config_value

def add_parser(sub_parsers) -> None:
    rename_parser = sub_parsers.add_parser("rename")
    rename_parser.add_argument("lab_name", help="Lab")
    rename_parser.add_argument("current_box_name", help="Name of the current box/working directory")
    rename_parser.add_argument("new_box_name", help="Name of the new box/working directory")

def main(lab_name: str, current_box_name: str, new_box_name: str) -> None:
    current_box_dir = Path(get_config_value("note_dir")) / lab_name / current_box_name
    new_box_dir = Path(get_config_value("note_dir")) / lab_name / new_box_name


    if current_box_dir.is_dir():
        current_box_dir.rename(new_box_dir)
        return

    print(f"Could not rename notes directory for {current_box_dir}! (Does not exist)")
