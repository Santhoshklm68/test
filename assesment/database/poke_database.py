
from pony.orm import Database, Required, PrimaryKey, db_session, commit


db=Database()

class Pokemon(db.Entity):
    _table_="pokers"
    name=Required(str)
    p_type=Required(str)
    





db.bind(provider='sqlite', filename='poker_db', create_db=True)

db.generate_mapping(create_tables=True)

with db_session:
    Pokemon(name='ronaldo', p_type='player')
    Pokemon(name='messi', p_type='soccer')
commit()



