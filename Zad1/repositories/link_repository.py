import csv
from io import TextIOWrapper
from models.Link import Link
from utils.file_reader import read_file


def parse(wrapper: TextIOWrapper) -> list:
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    return [Link(int(row[0]), row[1], row[2]) for row in reader]


def get_link_data():
    return parse(read_file("links.csv"))
