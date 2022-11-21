import csv
from io import TextIOWrapper
from models.Tag import Tag
from utils.file_reader import read_file


def parse(wrapper: TextIOWrapper) -> list:
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    return [Tag(int(row[0]), int(row[1]), row[2], row[3]) for row in reader]


def get_tag_data():
    return parse(read_file("tags.csv"))
