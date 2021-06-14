_FILE_TO_TAG_DICT = {
    "nmap": "<nmap/>",
    "gobust": "<gobust/>",
    "vhost": "<vhost/>",
    "hashes": "<hashes/>"
}


def add_parser(sub_parsers) -> None:
    import_parser = sub_parsers.add_parser("import")
    import_parser.add_argument("path_to_file", help="Path to the file to import")
    import_parser.add_argument("--tag", help="Tag to substitute in the markdown (e.g. 'nmap' to subsitute '<nmap/>' in the markdown)", dest="tag", default=None)

def main(path_to_file, tag=None):
    pass
