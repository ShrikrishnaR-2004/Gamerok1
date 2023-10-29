import sqlalchemy
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative

Base = sqlalchemy.orm.declarative_base()

engine = create_engine("mysql+pymysql://root:password@localhost/gamelist?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()
def load_games_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from games"))
        games = []
        for row in result.all():
            games.append(row._asdict())
        return games


@sqlalchemy.orm.as_declarative()
class Base:
    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class games(Base):

    __tablename__= 'games'

    Sr_no=sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    Game_Id = sqlalchemy.Column(sqlalchemy.String(5), primary_key=True)
    Game_Name = sqlalchemy.Column(sqlalchemy.String(80))
    Production = sqlalchemy.Column(sqlalchemy.String(50))
    Description = sqlalchemy.Column(sqlalchemy.String(500))
    Reviews = sqlalchemy.Column(sqlalchemy.String(500))
    Platforms = sqlalchemy.Column(sqlalchemy.String(500))
    Requirements = sqlalchemy.Column(sqlalchemy.String(500))
    Learn_more = sqlalchemy.Column(sqlalchemy.String(500))
    Playthrough_hours= sqlalchemy.Column(sqlalchemy.INTEGER)


Session = sessionmaker(bind=engine)
session = Session()

def getresult(search):

    #sql = sqlalchemy.text("SELECT * FROM @games AS g WHERE g.Game_Name =: value")
    #sql= games.select().where(games.Game_name==value)
    #result = conn.execute(sql, value=search)
    result = session.query(games).filter(games.Game_Name.like(search))
    #result = conn.execute(text("select * from games where Game_Name like 'Halo'"))

    '''rows = result.all()
    if len(rows) == 0:
        return None
    else:
        for r in result:
            return r.Game_Name, r.Production, r.Description, r.Reviews, r.Platforms, r.Requirements, r.Learn_more, r.Playthrough_hours
    r=result.all()
    return r._asdict()'''

    r=[]
    for row in result.all():
        r.append(row._asdict())
    return r

