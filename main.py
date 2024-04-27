"""TBW"""

import argparse


def main():
    """Main driver for the PDF Site project."""
    parser = argparse.ArgumentParser(
        prog="PDF Site",
        description="TBW",
    )

    parser.add_argument(
        "root_uri",
        type=str,
        help="The root URI for scraping",
    )

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
