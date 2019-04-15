from cassandra.cluster import Cluster
from cassandra import InvalidRequest


def create_session():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    return cluster, session


def insert(query, records, session):
    """
    Inserts all records with query in cursor.
    """
    for record in records:
        try:
            session.execute(query, record)
        except InvalidRequest as e:
            pass
