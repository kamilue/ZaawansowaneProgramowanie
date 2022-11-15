from flask import Flask
from flask_restful import Api
from routes.HomeRoute import HomeRoute
from routes.MovieRoute import MovieRoute

app = Flask(__name__)
api = Api(app)

api.add_resource(HomeRoute, '/')
api.add_resource(MovieRoute, '/movies')

if __name__ == '__main__':
    app.run(debug=True)
