#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """aaaa"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """aaaa"""

        diccionarito = dict()

        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(Amenity).all())
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)

        for PEPE1 in obj:
            return ("{}.{}".format(type(PEPE1).__name__, PEPE1.id))
        
    def new(self, obj):
        """aaaa"""

        self.__session.add(obj)

    def save(self):
        """aaaa"""

        self.__session.commit()

    def delete(self, obj=None):
        """aaaa"""
        
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """aaaa"""
        Base.metadata.create_all(self.__engine)
        sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessions)
        self.__session = Session()

    def close(self):
        """aaaa"""
        self.__session.close()