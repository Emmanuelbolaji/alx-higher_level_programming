#!/usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="monay")
    parser.add_argument("numbers", nargs="+", type=int, help="addddd")
    args = parser.parse_args()
    add = sum(args.numbers)
    print(add)

if __name__ == "__main__":
    main()
