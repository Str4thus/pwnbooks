def add_parser(sub_parsers) -> None:
    own_parser = sub_parsers.add_parser("own")
    own_parser.add_argument("type", help="Type of flag")
    own_parser.add_argument("flag", help="Flag value")


def main(type, flag):
    pass
