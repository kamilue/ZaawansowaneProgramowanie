from flask import Flask
from flask_restful import Api
from routes.HomeRoute import HomeRoute
from routes.MovieRoute import MovieRoute
from routes.LinkRoute import LinkRoute
from routes.RatingRoute import RatingRoute
from routes.TagRoute import TagRoute

app = Flask(__name__)
api = Api(app)

api.add_resource(HomeRoute, '/')
api.add_resource(MovieRoute, '/movies')
api.add_resource(LinkRoute, '/links')
api.add_resource(RatingRoute, '/ratings')
api.add_resource(TagRoute, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
