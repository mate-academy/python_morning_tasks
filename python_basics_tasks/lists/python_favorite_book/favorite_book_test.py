import ast
import subprocess

import favorite_book


TESTED_FILE = favorite_book
VAR_NAME = "list_of_books"
BOOK_LIST = ["The Lord of the Rings", "1984", "The Great Gatsby"]


def test_list_variable_is_defined():
    assert hasattr(
        TESTED_FILE, VAR_NAME
    ), f"Failed. Variable {VAR_NAME} should be defined"

    books = getattr(TESTED_FILE, VAR_NAME)

    assert isinstance(books, list), f"Failed. Variable {VAR_NAME} should be type <list>"
    assert len(books) == len(
        BOOK_LIST
    ), f"Failed. In {VAR_NAME} you should only change <1984> with your favorite book and not add additional books."
    assert isinstance(
        books[1], str
    ), f"Faield. In {VAR_NAME} your favorite book should be type <str>. Output: {books[1]}"
    assert (
        books[1] != BOOK_LIST[1]
    ), f"Failed. You should change <1984> with your favorite book. Your result list = {books}"


def test_result_list_was_printed():
    books = getattr(TESTED_FILE, VAR_NAME)

    process = subprocess.Popen(["python", "favorite_book.py"], stdout=subprocess.PIPE)
    captured_string_output = process.communicate()[0].decode()
    assert (
        captured_string_output
    ), "Failed. Result should be printed out with 'print()' function"

    printed_output_raw = ast.literal_eval(captured_string_output)
    assert printed_output_raw == books, f"Failed. {printed_output_raw} != {books}"
