#!/usr/bin/python3

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a connection with MySQL
        and create tables
        """

        db = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(db, pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)