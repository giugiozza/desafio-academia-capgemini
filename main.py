import sqlite3
from utility.utility import *


def main():
    while True:
        try:
            menu()
        except ValueError:
            print("Apenas números são válidos. Tente novamente.")


if __name__ == '__main__':
    main()
