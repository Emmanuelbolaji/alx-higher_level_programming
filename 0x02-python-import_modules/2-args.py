#!/usr/bin/python3
import sys


def main():
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print(f"0 arguments.")
    elif num_arg == 1:
        print("1 argument")
        print(f"1: {sys.argv[1]}")
    elif num_arg > 1:
        count = 0
        print(f"6 arguments:")
        for arg in sys.argv[1:]:
            count += 1
            print(f"{count}: {arg}")


if __name__ == "__main__":
    main()
