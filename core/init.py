import os
import shutil
from pathlib import Path
from .config import get_config_value, set_config_value

def add_parser(sub_parsers) -> None:
    init_parser = sub_parsers.add_parser("init")
    init_parser.add_argument("lab_name", help="Lab")
    init_parser.add_argument("box_name", help="Name of the box")
    init_parser.add_argument("--template", help="Template to generate the basic layout from (Default = 'ctf')", dest="template", default="ctf")
    init_parser.add_argument("--ip", "--target", help="IP of the box", dest="target", default=None)


def main(lab_name: str, box_name: str, template="ctf", target=None) -> None:
    target_dir = Path(get_config_value("root_path")) / get_config_value("lab_dir") / lab_name / (f"{box_name} ({target})" if target else box_name)
    template_dir = Path(get_config_value("root_path")) / get_config_value("template_dir") / template

    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

        for f in os.listdir(template_dir):
            shutil.copy(template_dir / f, target_dir)

    