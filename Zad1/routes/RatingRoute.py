from flask_restful import Resource
from repositories.rating_repository import get_rating_data
from utils.json_extension import to_json, to_json_string


class RatingRoute(Resource):
    def get(self):
        return to_json(to_json_string(get_rating_data()))
