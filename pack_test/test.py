#!/usr/bin/env python3
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from pack_test.kadaie_1 import kadaie_1


def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Test script for uv packaging.",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="fasta files you want to check",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-l", "--length", help="length you want to check", type=int, required=True
    )

    args = parser.parse_args()
    kadaie_1(args.input, args.length)


if __name__ == "__main__":
    main()
