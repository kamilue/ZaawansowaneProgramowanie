from flask_restful import Resource


class MovieRoute(Resource):
    def get(self):
        return {"movie": "movie"}
