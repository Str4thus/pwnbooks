import os
from datetime import datetime
from argparse import ArgumentParser
from pathlib import Path
from core.config import get_config_value


def add_parser(sub_parsers: ArgumentParser) -> None:
    blog_init_parser = sub_parsers.add_parser("blog_init")
    
    blog_init_parser.add_argument("folder", help="Folder Name")
    blog_init_parser.add_argument("title", help="Post Title")


def main(folder: str, title: str) -> None:
    blog_dir = Path(get_config_value("blog_dir"))

    if blog_dir.exists():
        os.system(f"cd {blog_dir}; git pull")
    
    blog_dir /= folder

    try:
        blog_dir.mkdir()
    except (FileExistsError):
        print(f"The blogpost {folder} already exists!")
        return

    post_file = Path(blog_dir, f"{title}.md")
    with post_file.open(mode="w") as f:
        f.write(f"""
            # {title}
        """)

    print(f"Created blogpost '{title}' at {blog_dir}")
