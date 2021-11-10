import os
import unittest
from typing import TextIO


def write_file(filename: str, text: str, encoding: str) -> str:
    file: TextIO = open(file=filename, mode='a', encoding=encoding)
    file.write(text)
    file.close()
    return filename


def read_file(filename: str, encoding: str) -> list[str]:
    file: TextIO = open(file=filename, mode='r', encoding=encoding)
    readlines: list[str] = file.readlines()
    file.close()
    return readlines


class FileTest(unittest.TestCase):

    def test_read_write(self) -> None:
        # Arrange
        filename: str = 'filename'
        text: str = 'hello unit test'
        encoding: str = 'utf-8'

        # Assert
        write_filename: str = write_file(filename=filename, text=text, encoding=encoding)
        file_content: list[str] = read_file(filename=write_filename, encoding=encoding)

        # Act
        self.assertEqual(text, file_content[0])

    def tearDown(self) -> None:
        os.remove(path='filename')


if __name__ == '__main__':
    unittest.main()
