import string
import shutil
import re

from .blog_update import update_blog

from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value



def add_parser(sub_parsers: ArgumentParser) -> None:
    blog_sync_parser = sub_parsers.add_parser("blog_sync")

    blog_sync_parser.add_argument("-u", help="Automatically update the blog repo", dest="auto_update", action="store_true")


def _replace_image_links(writeup_path):
    with open(writeup_path, "r") as f:
        content = f.read()
        replaced_content = re.sub("\]\(P", "](./P", content, flags=re.M)

    with open(writeup_path, "w") as f:
        f.write(replaced_content)

def _add_entry_to_summary(lab_name, box_name):
    blog_dir = Path(get_config_value("blog_dir"))

    lab_entry = f"* [{lab_name.upper()}]({lab_name}/README.md)\n"
    box_entry = f"    * [{box_name.capitalize()}]({lab_name}/{box_name}/{box_name}.md)\n"

    with open(blog_dir / "SUMMARY.md", "r") as summary:
        entries = [entry for entry in summary.readlines()]

    # Check if lab already exists
    lowercase_entries = [entry.lower() for entry in entries]
    if lab_entry.lower() not in lowercase_entries:
        entries.append(lab_entry)


    lowercase_entries = [entry.lower() for entry in entries]
    # Check if writeup already exists
    if box_entry.lower() not in lowercase_entries:
        lab_entry_index = lowercase_entries.index(lab_entry.lower())

        if lab_entry_index == len(entries)+1:
            entries.append(box_entry)
        else:
            entries.insert(lab_entry_index+1, box_entry)


    with open(blog_dir / "SUMMARY.md", "w") as summary:
        for entry in entries:
            summary.write(entry)


def _copy_writeup_folders(lab_name, box_name, writeup_dir):
    blog_dir = Path(get_config_value("blog_dir"))
    blog_lab_dir = blog_dir / lab_name
    blog_box_dir = blog_dir / lab_name / box_name

    if not blog_lab_dir.exists():
        blog_lab_dir.mkdir()
        initial_readme_md = blog_lab_dir / "README.md"
        initial_readme_md.touch()
    
    if not blog_box_dir.exists():
        blog_box_dir.mkdir()

    # Copy Writeup
    writeup_md = writeup_dir / "Writeup.md"
    target_writeup_path = blog_box_dir / f"{box_name.lower()}.md"
    shutil.copyfile(writeup_md, target_writeup_path)

    # Copy Images
    writeup_image_dir = writeup_dir / "img"

    if writeup_image_dir.exists():
        shutil.copytree(writeup_image_dir, blog_box_dir, dirs_exist_ok=True)

    _add_entry_to_summary(lab_name, box_name)
    _replace_image_links(target_writeup_path)


def main(auto_update: bool=False) -> None:
    note_dir = Path(get_config_value("note_dir"))
    blog_dir = Path(get_config_value("blog_dir"))

    if not note_dir.exists():
        print(f"{note_dir} does not exist!")
    if not blog_dir.exists():
        print(f"{blog_dir} does not exist!")

    lab_dirs = []
    for child in note_dir.iterdir():
        if child.stem[0] not in string.punctuation:
            lab_dirs.append(Path(child))


    # Find Writeup files
    for lab_dir in lab_dirs:
        for box_dir in lab_dir.iterdir():
            if box_dir.is_dir():
                for box_notes in box_dir.iterdir():
                    if box_notes.stem == "-> Writeup":
                        writeup_dir = box_notes

                        _copy_writeup_folders(lab_dir.stem, box_dir.stem, writeup_dir)

    if auto_update:
        update_blog()
        
