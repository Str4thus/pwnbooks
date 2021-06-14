# pwnbooks.py blog update
# -> commit and push to repo
import os
from datetime import datetime
from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value


def add_parser(sub_parsers: ArgumentParser) -> None:
    blog_init_parser = sub_parsers.add_parser("blog_init")
    
    blog_init_parser.add_argument("box_name", help="Name of the box")
    blog_init_parser.add_argument("title", help="Post Title")
    blog_init_parser.add_argument("slug", help="Folder Name")

def main(box_name: str, title: str, slug: str) -> None:
    blog_dir = Path(get_config_value("blog_dir"))

    if blog_dir.exists():
        os.system(f"cd {blog_dir}; git pull")
    
    blog_dir /= slug

    try:
        blog_dir.mkdir()
    except (FileExistsError):
        print(f"The blogpost {slug} already exists!")

    item_md = Path(blog_dir, "item.md")
    with item_md.open(mode="w") as item_file:
        item_file.write(f"""
---
title: '{title}'
date: '{datetime.now().strftime("%d-%m-%Y %H:%M")}'
author: Str4thus
hero_classes: 'text-light title-h1h2 parallax overlay-dark-gradient hero-large'
hero_image: {box_name}.png
show_sidebar: true
feed:
    limit: 10
---

<summary>

===

---

<content>

""")
