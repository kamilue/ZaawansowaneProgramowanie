import csv
from io import TextIOWrapper
from models.Rating import Rating
from utils.file_reader import read_file


def parse(wrapper: TextIOWrapper) -> list:
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    return [
        Rating(int(row[0]), int(row[1]), float(row[2]), row[3])
        for row in reader
    ]


def get_rating_data():
    return parse(read_file("ratings.csv"))
