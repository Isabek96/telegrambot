import psycopg2
from psycopg2.extras import RealDictCursor
from config import host, user, password, database

connection = None

def connect_db():
    global connection
    if connection is None or connection.closed != 0:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursor_factory=RealDictCursor  # чтобы получать dict, а не tuple
        )

def get_connection():
    if connection is None or connection.closed != 0:
        connect_db()
    return connection
