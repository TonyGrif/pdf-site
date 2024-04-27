"""TBW"""

import argparse

import requests


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

    try:
        response = requests.get(args.root_uri)
    # TODO: Specificity
    except Exception:
        parser.exit(-1, "Invalid root URI supplied\n")
    assert response.status_code == 200


if __name__ == "__main__":
    main()
