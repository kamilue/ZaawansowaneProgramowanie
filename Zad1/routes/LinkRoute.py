from flask_restful import Resource
from repositories.link_repository import get_link_data
from utils.json_extension import to_json, to_json_string


class LinkRoute(Resource):
    def get(self):
        return to_json(to_json_string(get_link_data()))
