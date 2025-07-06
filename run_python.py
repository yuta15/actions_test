import json
import sys
import os
import argparse


def main(args: str):
    data = {
        "config": {
            "test": args
        }
    }
    os.mkdir("test")
    with open("test/config.json", "w") as f:
        json.dump(data, f, indent=4)
    sys.stdout.write(os.path.dirname(os.path.abspath("test/config.json")))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Python script with a given path.')
    parser.add_argument('arg1', type=str, help='The path to the Python script to run.')
    args = parser.parse_args()
    main(args.arg1)