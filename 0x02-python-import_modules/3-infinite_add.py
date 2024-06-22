#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="addition")
    parser.add_argument("numbers", nargs="+", type=int, help="adding all numbers")
    args = parser.parse_args()
    add = sum(args.numbers)
    print(f"{add}")


if __name__ == "__main__":
    main()
