import os

from etl.etl import Etl

FILES_PATH = '../files_to_read/'

if __name__ == '__main__':
    with os.scandir(FILES_PATH) as entries:
        for idx, entry in enumerate(entries):
            Etl.run(f'{FILES_PATH}{entry.name}')
