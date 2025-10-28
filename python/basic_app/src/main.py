#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple Python app")
    parser.add_argument('--name', '-n', default='World', help='Name to greet')
    args = parser.parse_args()
    print(f"Hello, {args.name} from Python!")


if __name__ == '__main__':
    main()
