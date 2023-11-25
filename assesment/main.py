from flask import Flask
from flask_restx import Api, Resource, fields
from methods.poke_method import api, ns as pokie_users
from database.poke_database import db




app = Flask(__name__)
api.init_app(app)
api.add_namespace(pokie_users)




if __name__ == '__main__':
    app.run(debug=True)