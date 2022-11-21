import csv
from io import TextIOWrapper
from models.Movie import Movie
from utils.file_reader import read_file


def parse(wrapper: TextIOWrapper) -> list:
    reader = csv.reader(wrapper, delimiter=",")
    next(reader)
    return [Movie(int(row[0]), row[1], row[2]) for row in reader]


def get_movie_data():
    return parse(read_file("movies.csv"))
