from flask import request
from flask_restx import Api, Resource, fields, reqparse
from database.poke_database import Pokemon
from pony.orm import db_session, select, commit, Json
from enum import Enum



api=Api()
ns=api.namespace('pokie')

class PokemonType(Enum):
    FIRE = 'fire'
    WATER = 'water'
    GRASS = 'grass'

parser=reqparse.RequestParser()

poke_fields = api.model ('Pokemon', {
    'name':fields.String(),
    'type':fields.Integer(attribute='p_type'),
    
    
})


@ns.route('/')
class PokerResource(Resource):
    # @ns.expect(parser)
    @db_session
    @ns.marshal_list_with(poke_fields)
    
    def get(self):
        query = select(p for p in Pokemon)
        return query
   
    @db_session
    @ns.expect(parser)
    @ns.marshal_list_with(poke_fields)
    def post(self):
        
        args = parser.parse_args()
        
        ans = args['name'], args['type']
        commit()
        return ans
    




    



