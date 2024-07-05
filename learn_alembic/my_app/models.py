from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class emp(Base):
    __tablename__ = 'emp'
    emp_id = Column(Integer, primary_key=True)
    department_id = Column(Integer)


# # DEFINE THE DATABASE CREDENTIALS
# user = 'root'
# password = ''
# host = '127.0.0.1'
# port = 3306
# database = 'dataanalyst'

# # PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# # RETURN THE SQLACHEMY ENGINE OBJECT


# def get_connection():
#     return create_engine(
#         url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )


# # Example of creating an engine (use your actual database URI)
# engine = get_connection()
# Base.metadata.create_all(engine)
