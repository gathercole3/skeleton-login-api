from skeleton_login_api import db
from sqlalchemy import create_engine
from skeleton_login_api.models import Users
from sqlalchemy.orm import sessionmaker
from skeleton_login_api import config


class Sql:
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                   pool_size=20, max_overflow=0)
    Session = sessionmaker(bind=engine, autoflush=False)

    # create a Session
    session = Session()

    def try_commit():
        try:
            Sql.session.commit()
        except:
            Sql.session.rollback()

#start of search sql statements
    def get_user(params):
        return Sql.session.query(Users).filter_by(**params).all()

#start of insert sql statments
    def new_user(params):
        new_user = Users(**params)
        Sql.session.add(new_user)
        Sql.try_commit()
        return Sql.get_user(new_user.to_dict())


#start of update sql statments


db.engine.dispose()
