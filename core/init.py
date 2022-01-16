import os
import shutil
from pathlib import Path
from .config import get_config_value, set_config_value


def add_parser(sub_parsers) -> None:
    init_parser = sub_parsers.add_parser("init")
    init_parser.add_argument("lab_name", help="Lab")
    init_parser.add_argument("box_name", help="Name of the box")
    init_parser.add_argument("--template", help="Template to generate the basic layout from (Default = 'ctf')", dest="template", default="ctf")

def main(lab_name: str, box_name: str, template="ctf") -> None:
    target_dir = Path(get_config_value("note_dir")) / lab_name / box_name
    template_dir = Path(get_config_value("template_dir")) / template

    os.system(f"cd {get_config_value('note_dir')}; git pull 1>/dev/null")

    if os.path.isdir(target_dir):
        print(f"Notes for '{box_name}' already exist!")   
        return
 
    shutil.copytree(str(template_dir), str(target_dir), copy_function = shutil.copy)
