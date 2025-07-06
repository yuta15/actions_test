import sys
import os
import argparse


def main(args: str):
    sys.stdout.write(f'{args}testのmain関数')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Python script with a given path.')
    parser.add_argument('arg1', type=str, help='The path to the Python script to run.')
    args = parser.parse_args()
    main(args.arg1)